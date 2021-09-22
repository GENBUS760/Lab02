import boto3

s3 = boto3.resource('s3', aws_access_key_id= "AKIASM2MBGFS743GSEPX", aws_secret_access_key= "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")

s3.create_bucket(Bucket='lsybucket579')

s3.meta.client.upload_file('/home/parallels/Desktop/GB760/Lab02/123.py', 'lsybucket579', '123.py') 
