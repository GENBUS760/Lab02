#importing libraries
import boto3

#initializing s3 resource high level 
s3 = boto3.resource('s3',
         aws_access_key_id= 'AKIATJCQYOMEXELKNPXX',
         aws_secret_access_key= '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')

#creating a bucket
s3.create_bucket(Bucket='msawan2bucketlab02', CreateBucketConfiguration={
    'LocationConstraint': 'us-east-2'})

#storing data from a file    
s3.Object('msawan2bucketlab02', 'test.txt').put(Body=open('test.txt', 'rb'))

