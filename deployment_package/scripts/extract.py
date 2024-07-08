import requests
import yaml
import logging
import sys

# Setup logger
logger = logging.getLogger("extract")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def fetch_weather_data(api_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()
    return data

def extract_weather_data(config):
    api_key = config["weather_api"]["api_key"]
    cities = config["weather_api"]["cities"]

    weather_data = []
    for city in cities:
        data = fetch_weather_data(api_key, city)
        weather_data.append(data)
        logger.info(f"Fetched data for city: {city}")
    
    return weather_data
