from boto3.session import Session
import boto3
access_key='AKIAQ765WI33FDYWZHFS'
secret_key='cIuN0Lg\/PYK1y69Hdsy9Pgfh\/0jvYoeUxobS9voC'
url='http://oss-cnbj01.cdsgss.com'
session=Session(access_key,secret_key)
s3_client=session.client('s3',endpoint_url=url)

s3_client.create_bucket(Bucket='yunfan111222')
resp=s3_client.put_object(Bucket='yunfan111222',Key='yunfanzzz',Body=open('aaa.txt','rb').read())
