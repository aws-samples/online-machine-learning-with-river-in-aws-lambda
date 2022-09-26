# Welcome to your serverless online machine learning repository using River!

This app creates a stack (`river_app_stack`) which contains an Amazon S3 bucket and an AWS Lambda
function that runs online machine learning in a serverless fashion. Your model(s) will be stored
in Amazon S3 for you.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project. First we will need to create a virtuelenv,
stored under a .venv directory.  To create the virtualenv it assumes that there is a `python3` executable
in your path with access to the `venv` package.

Set the name of your stack and Amazon S3 bucket in app.py, e.g.:

```
RiverAppStack(app, "STACK_NAME", bucket_name='BUCKET_NAME')
```

Create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

And of course deploy the stack:

```
$ cdk deploy
```

You can now begin exploring the source code, contained in the river_app directory.
Further unit tests are including and can be run through:

```
$ pytest
```

To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
