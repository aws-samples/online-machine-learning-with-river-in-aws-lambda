from constructs import Construct
import aws_cdk as _cdk
from aws_cdk import (
    Stack,
    Duration,
    aws_lambda as _lambda,
    aws_s3 as _s3,
)

class RiverAppStack(Stack):

    def __init__(self, scope: Construct, id: str, bucket_name: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        dockerfile = "lambda/drift_detection/"
        
        bucket = _s3.Bucket(
            self,
            f"{bucket_name}Asset",
            bucket_name=bucket_name,
            server_access_logs_bucket=self,
            server_access_logs_prefix="logging-",
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=_cdk.RemovalPolicy.RETAIN,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            enforce_ssl=True)

        # Defines an AWS Lambda resource
        drift_detection_lambda = _lambda.DockerImageFunction(
            self,
            'DriftDetection',
            code=_lambda.DockerImageCode.from_image_asset(dockerfile),
            environment={
                'BUCKET': bucket.bucket_name,
            },
            timeout=Duration.seconds(60),
        )
        
        bucket.grant_read(drift_detection_lambda)
        bucket.grant_write(drift_detection_lambda)