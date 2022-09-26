import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="river_app_library",
    version="1.0.0",

    description="This library deploys various river compontents in a serverless fashion for you.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Michael Wallner",

    package_dir={"": "river_app"},
    packages=setuptools.find_packages(where="river_app"),

    install_requires=[
        "aws-cdk-lib==2.38.1",
        "cdk-nag==2.16.0",
        "constructs>=10.0.0,<11.0.0",
        "pytest==6.2.5",
        "boto3"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: MIT-0 License",

        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
