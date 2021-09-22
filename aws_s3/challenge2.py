#source: 
import os
import boto3

from dotenv import load_dotenv
load_dotenv(verbose=True)


def aws_session(region_name='us-east-1'):
    return boto3.session.Session(aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                                aws_secret_access_key=os.getenv('AWS_ACCESS_KEY_SECRET'),
                                region_name=region_name)
session = aws_session()
s3_resource = session.resource('s3')

def make_bucket(name):
    session = aws_session()
    s3_resource = session.resource('s3')
    return s3_resource.create_bucket(Bucket=name)

s3_bucket = make_bucket('yujiading')
