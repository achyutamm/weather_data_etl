import json
import yaml
from scripts.extract import extract_weather_data
from scripts.transform import transform_weather_data
from scripts.load import load_weather_data
from utils.logger import setup_logger

logger = setup_logger("etl_lambda")

def lambda_handler(event, context):
    try:
        # Load configuration
        logger.info("Loading configuration")
        with open('config/config.yaml', 'r') as config_file:
            config = yaml.safe_load(config_file)

        # Extract data
        logger.info("Starting data extraction")
        raw_data = extract_weather_data(config)
        logger.info("Data extraction completed")

        # Transform data
        logger.info("Starting data transformation")
        transformed_data = transform_weather_data(raw_data)
        logger.info("Data transformation completed")

        # Load data
        logger.info("Starting data loading")
        load_weather_data(config, transformed_data)
        logger.info("Data loading completed")

        return {
            'statusCode': 200,
            'body': json.dumps('ETL process completed successfully!')
        }
    except Exception as e:
        logger.error(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {e}")
        }
