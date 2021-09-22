import boto3

#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id='AKIAUH6QNWKE73F22REZ',
aws_secret_access_key='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'
)

#Creating S3 Resource From the Session.
s3 = session.resource('s3')

object = s3.Object('datatechnology', 'test.txt')

txt_data = b'This is the content of the file uploaded from python boto3 asdfasdf'

result = object.put(Body=txt_data)

