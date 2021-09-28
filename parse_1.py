import boto3

#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id='AKIA2F3MUJ3YSKQD5OQU',
aws_secret_access_key='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'
)

#Creating S3 Resource From the Session.
s3 = session.resource('s3')

object = s3.Object('shifan42', '05_github.py')

result = object.put()
