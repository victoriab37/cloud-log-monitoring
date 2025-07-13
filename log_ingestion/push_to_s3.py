import boto3
import json
import os

# Set up AWS S3 client
s3 = boto3.client('s3')

# File to upload
file_name = 'security_logs.json'
bucket_name = 'mini-siem-logs'  # Replace with your actual S3 bucket name
object_name = f"logs/{file_name}"      # Upload path in S3

def upload_to_s3():
    try:
        s3.upload_file(file_name, bucket_name, object_name)
        print(f"✅ Successfully uploaded {file_name} to s3://{bucket_name}/{object_name}")
    except Exception as e:
        print(f"❌ Upload failed: {e}")

if __name__ == "__main__":
    upload_to_s3()
