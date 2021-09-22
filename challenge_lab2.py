import boto3

s3 = boto3.resource("s3")
bucket = s3.create_bucket(Bucket="my_bucket")
bucket.name

