import logging
import sys

# Setup logger
logger = logging.getLogger("transform")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def transform_weather_data(raw_data):
    transformed_data = []
    for data in raw_data:
        transformed_record = {
            "city": data["location"]["name"],
            "temperature": data["current"]["temp_c"],
            "humidity": data["current"]["humidity"],
            "timestamp": data["location"]["localtime"]
        }
        transformed_data.append(transformed_record)
        logger.info(f"Transformed data for city: {data['location']['name']}")
    return transformed_data
