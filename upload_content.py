import boto3
import os

s3 = boto3.client('s3')
bucket_name = 'your-unique-bucket-name'

def upload_file(file_path):
    s3.upload_file(file_path, bucket_name, os.path.basename(file_path))
