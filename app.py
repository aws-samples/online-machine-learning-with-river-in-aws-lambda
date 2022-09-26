#!/usr/bin/env python3

import aws_cdk as _cdk
import cdk_nag as _nag

from river_app.river_app_stack import RiverAppStack

app = _cdk.App()
RiverAppStack(
	app,
	"STACK_NAME",
	bucket_name='BUCKET_NAME')

# Uncomment for nag testing:
# _cdk.Aspects.of(app).add(_nag.AwsSolutionsChecks())

app.synth()
