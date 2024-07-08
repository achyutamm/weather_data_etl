import boto3

def list_s3_bucket_contents(bucket_name, prefix=''):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    
    if 'Contents' in response:
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print("No objects found in the bucket.")

# Replace 'your-bucket-name' with your actual bucket name and 'weather_data/' with your folder prefix
list_s3_bucket_contents('weather-etl-bucket', 'weather_data/')
