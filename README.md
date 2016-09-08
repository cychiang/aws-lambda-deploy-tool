# Introduction
AWS Lambda is the powerful service which can help you to deploy your serverless services.
However, if you want to create a function that contains third party libraries.
You will need to build your own environment on AWS EC2 instance with offical AMI.
The aim of this tool is to provide a base zip file which generates from AWS EC2.

All zip files are built on AWS EC2 with AMI: "amzn-ami-hvm-2016.03.3.x86_64-gp2"

# How To Use?
Just simply appach your Python file into base zip file. Than upload into AWS Lambda service.

# Description of zip files.
Base zip files are store on "zip-files" folder.

## bigquery-mysql-base.zip 
- [BigQuery-Python 1.8.0](https://github.com/tylertreat/BigQuery-Python)
- [PyMySQL 0.7.9](https://github.com/PyMySQL/PyMySQL)
