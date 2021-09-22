'''
import logging
import boto3
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region=None):
	try:
		if region is None:
			S3_client = boto3.client('S3')
			S3_client.create_bucket(Bucket = gb760)
		else:
			S3_Client = boto3.client('S3', region_name = region)
			location = {'LocationConstraint': region}
			S3_client.create_bucket(Bucket = gb760, CreateBucketConfiguration = Location)
	except ClientError as e:
		logging.error(e)
		return Flase
	return True
'''
# The code above are from AWS official website.

client = boto3.client(
    's3',
    aws_access_key_id = 'AKIA3QNTL6E2JRVAC6IH',
    aws_secret_access_key = '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',
    region_name = None
)

clientResponse = client.list_buckets()
