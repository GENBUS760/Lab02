import boto3
import pandas as pd
session=boto3.session.Session()
#cited from:http://docs.ceph.org.cn/radosgw/s3/python/   
#since I have no AWS account, so I have no idea about access_key and secret_key....
access_key =input( 'put your access key here!')
secret_key = input('put your secret key here!')
endpoint=input('put your endpoint url here!')
#cited from https://www.bilibili.com/video/BV1jV411C7dK?spm_id_from=333.1007.top_right_bar_window_history.content.click
file_path='/home/gb760/Lab02/Lab02/7974.T.csv'
key_name='7974.T.csv'
bucket_name='Lab02"
s3=session.client('s3',use_ssl=False,endpoint_url=endpoint,aws_access_key_id=access_key,aws_secret_key_id=secret_key)
response = s3.create_bucket(Bucket=bucket_name)
s3.upload_file(file_path,bucket_name,key_name	)
