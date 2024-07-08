import boto3
import json
from utils.logger import setup_logger

logger = setup_logger("load")

def load_weather_data(config, weather_data):
    s3_config = config["s3"]
    bucket_name = s3_config["bucket_name"]
    folder = s3_config["folder"]
    
    s3 = boto3.client('s3')
    
    for record in weather_data:
        city = record["city"]
        file_name = f"{folder}/{city}.json"
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json.dumps(record))
        logger.info(f"Uploaded data for city: {city}")

    logger.info("Data loading to S3 completed successfully")
