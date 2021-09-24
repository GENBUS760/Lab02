import boto3

'''
Edited 9/23
- Removed Personal Credential
- Added user input (key_id, secret_key)
'''

key_id = input('Please enter your aws_access_key_id:')
secret_key = input('Please enter your aws_secret_access_key:')

session = boto3.Session(
    aws_access_key_id=key_id,
    aws_secret_access_key=secret_key
)

s3 = session.resource('s3')
s3.create_bucket(Bucket='gb760lab02bucket')
txt_data = b'extra credit?'
object = s3.Object('gb760lab02bucket', 'hello.txt')
object.put(Body=txt_data)
