# Weather Data ETL Pipeline

## Overview
This project demonstrates an ETL (Extract, Transform, Load) pipeline to process weather data from a public API and store it in Amazon S3. The data is then queried using Amazon Athena.

## Technologies Used
- Python
- AWS CLI
- Amazon S3
- Amazon Athena

## Project Structure
weather_data_etl/
├── config/
│ └── config.yaml
├── scripts/
│ ├── extract.py
│ ├── transform.py
│ └── load.py
├── utils/
│ └── logger.py
├── etl_pipeline.py
├── requirements.txt
├── README.md
└── demo_video.mp4



## Setup Instructions

### Prerequisites
- AWS account
- Python 3.8+
- AWS CLI installed and configured

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/weather_data_etl.git
   cd weather_data_etl
