import boto3

session = boto3.Session(
    aws_access_key_id='AKIAVUY4Z73H2LF54INP',
    aws_secret_access_key='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'
)

s3 = session.resource('s3')
s3.create_bucket(Bucket='gb760lab02bucket')
txt_data = b'extra credit?'
object = s3.Object('gb760lab02bucket', 'hello.txt')
result = object.put(Body=txt_data)

