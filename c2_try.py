
import boto3

s3 = boto3.resource('s3', aws_access_key_id= "AKIAYZGTUG33MGS6V76A", aws_secret_access_key= "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")

s3.create_bucket(Bucket='efoirheoifehjiojklajkljfeaoijeriojroij')


s3.meta.client.upload_file('/home/gb760/parse.py', 'efoirheoifehjiojklajkljfeaoijeriojroij', 'hello.py')

