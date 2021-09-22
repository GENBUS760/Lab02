import boto3

s3 = boto3.resource('s3', aws_access_key_id= "AKIAXCLWW4HVEZUTRTKA", aws_secret_access_key= "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")

s3.create_bucket(Bucket='gjgj667745asasdasd')

s3.meta.client.upload_file('/home/gb760/Lab02/hello.txt', 'gjgj667745asasdasd', 'hello.txt')
