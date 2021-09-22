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

s3 = boto3.client('s3')
response = s3.list_buckets()

print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')


