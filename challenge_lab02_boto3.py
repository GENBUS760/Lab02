import boto3

AWS_ACCESS_KEY_ID = 'AKIAVH6DSILW4EGQJGAF'
AWS_ACCESS_SECRET_ACCESS_KEY = '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'

sess = boto3.Session(region_name='us-east-2',
		aws_access_key_id=AWS_ACCESS_KEY_ID, 
      	aws_secret_access_key=AWS_ACCESS_SECRET_ACCESS_KEY)

s3client = sess.client('s3')

bucket_name = 'datatechnologywisc'
s3_location = {
	'LocationConstraint': 'us-east-2'
}

s3client.create_bucket(Bucket=bucket_name, 
        CreateBucketConfiguration=s3_location,
        ACL='public-read')
