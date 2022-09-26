from aws_cdk import (
    Stack,
    Duration,
    assertions,
    aws_lambda as _lambda
)

from river_app.river_app_stack import RiverAppStack
import pytest


def test_lambda_has_env_vars():
    stack = Stack()
    tassert = assertions.Template.from_stack(RiverAppStack(stack, "drift-detection-app", bucket_name='test-s3-bucket'))
    envCapture = assertions.Capture()
    tassert.has_resource_properties("AWS::Lambda::Function", props={"Environment": envCapture})
    
def test_resources_created():
    stack = Stack()
    tassert = assertions.Template.from_stack(RiverAppStack(stack, "drift-detection-app", bucket_name='test-s3-bucket'))
    tassert.resource_count_is("AWS::S3::Bucket", 1)
    tassert.resource_count_is("AWS::Lambda::Function", 1)
    tassert.resource_count_is("AWS::IAM::Role", 1)
    tassert.resource_count_is("AWS::IAM::Policy", 1)

def test_s3_bucket_properties():
    stack = Stack()
    tassert = assertions.Template.from_stack(RiverAppStack(stack, "drift-detection-app", bucket_name='test-s3-bucket'))
    tassert.has_resource_properties("AWS::S3::Bucket", props={"BucketName": "test-s3-bucket"})