import boto3

# Creating the low level functional client
client = boto3.client(
    's3',
    aws_access_key_id = "AKIAUN6JRXCTE5ZDYPW6",
    aws_secret_access_key = "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",
    region_name = 'us-west-1'
)
    
# Creating the high level object oriented interface
resource = boto3.resource(
    's3',
    aws_access_key_id = "AKIAUN6JRXCTE5ZDYPW6",
    aws_secret_access_key = "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",
    region_name = 'us-west-1'
)

# Fetch the list of existing buckets
clientResponse = client.list_buckets()
    
# Print the bucket names one by one
print('Printing bucket names...')
for bucket in clientResponse['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')
    

# Creating a bucket in AWS S3
location = {'LocationConstraint': 'us-west-1'}
client.create_bucket(
    Bucket = 'challengea-lab02-1',
    CreateBucketConfiguration=location
)

# Create the S3 object
obj = client.get_object(
    Bucket = 'challengea-lab02-2',
    Key = 'challengea-lab02-FangshuoLiu.csv'
)
    
# Read data from the S3 object
data = pandas.read_csv(obj['Body'])
    
# Print the data frame
print('Printing the data frame...')
print(data)

s3 = boto3.resources("s3")
s3.Bucket("challengea-lab02-1").upload_file("/home/gb760/Lab02/hhh.txt","hhh.txt")




