import boto3
s3 = boto3.resource('s3')
s3.create_bucket(Bucket='mybucket', CreateBucketConfiguration={
    'LocationConstraint': 'us-west-1'})
# code from Stackoverflow
