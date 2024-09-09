import boto3

s3 = boto3.client('s3')
bucket_name = 'your-unique-bucket-name'

s3.create_bucket(Bucket=bucket_name)
