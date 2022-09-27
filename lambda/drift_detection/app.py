"""This is the main app that runs in your AWS Lambda function."""

# Import libraries
import tempfile 
import logging
import joblib
import base64
import json
import os

import boto3
import botocore
from io import BytesIO

import numpy as np
import pandas as pd
from river import drift

# Set Amazon S3 client
client = boto3.client("s3")

# Read env var: BUCKET
BUCKET = os.getenv("BUCKET")

def lambda_handler(event, context):
    """Main entry point for the AWS Lambda function.

    :event: Must contain 'body' and 'key' where
        'body' = the observed number from your machine
        'key' = the model location in your S3 bucket
    :context: The AWS Lambda context sent to the function.

    :return: The dict with status code and output_body

    """
    # Read the value from body and S3 key
    logging.info("Parse event...")
    val = float(event['body'])
    key = event['key']
    
    # Set default response
    output_body = {
        "Drift": "No"
    }
    
    # Initialize model - will be overwritten if
    # it already exists in Amazon S3. If it doesn't
    # this function will save a new empty model
    # for you.
    model = drift.ADWIN()
    
    # Check if model exists...
    try:
        # Load the model from Amazon S3
        logging.info("Load model...")
        response = client.get_object(
            Bucket=BUCKET,
            Key=key)
        r = BytesIO(response["Body"].read())
        model = joblib.load(r)

        # Update the model based on your newest observation
        logging.info("Update model...")
        model.update(val)
        
        # If drift is detected change the output
        logging.info("Detect changes...")
        if model.drift_detected:
            output_body["Drift"] = "Yes"
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            # Update the model based on your newest observation
            logging.info("Update model...")
            model.update(val)
            logging.info("Object does not exist yet. Creating...")
        else:
            logging.error("The Lambda function failed for another reason...")
            logging.error(e)

    # Store the updated model back on S3
    logging.info("Save model back to S3...")
    with tempfile.TemporaryFile() as fp:
        joblib.dump(model, fp)
        fp.seek(0)
        client.put_object(
            Body=fp.read(),
            Bucket=BUCKET,
            Key=key)
    
    # Return your response
    logging.info("Return...")
    return {
        'statusCode': 200,
        'body': json.dumps(output_body)
    }
