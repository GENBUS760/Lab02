import boto3

ses = boto3.Session(region_name='us-east-2',
aws_access_key_id='AKIAQAKTNXQDFMHTUCFH',
aws_secret_access_key='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')

sess3client = ses.client('s3')

bucketname = 'jawmadison071234'
location = {'LocationConstraint': 'us-east-2'}

sess3client.create_bucket(Bucket=bucketname, CreateBucketConfiguration=location)

