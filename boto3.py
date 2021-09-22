
import os
import boto3
import io

from dotenv import load_dotenv
load_dotenv(verbose=True)


def aws_session(region_name='us-east-2'):
    return boto3.session.Session(aws_access_key_id=os.getenv('AKIA2DLZY7OLIDJS5JHA'),
                                aws_secret_access_key=os.getenv('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'),
                                region_name=region_name)


def make_bucket(name, acl):
    session = aws_session()
    s3_resource = session.resource('s3')
    return s3_resource.create_bucket(Bucket=name, ACL=acl)


def upload_file_to_bucket(bucket_name, file_path):
    session = aws_session()
    s3_resource = session.resource('s3')
    file_dir, file_name = os.path.split(file_path)

    bucket = s3_resource.Bucket(bucket_name)
    bucket.upload_file(
      Filename=file_path,
      Key=file_name,
      ExtraArgs={'ACL': 'public-read'}
    )

    s3_url = f"https://datatech.s3.us-east-2.amazonaws.com/Chanllenge2.py"
    return s3_url

