# Exchange Rate ETL Pipeline

A simple ETL pipeline that pulls live exchange rate data from public API and stores it in a PostgreSQL database

## What It Does

- **Extract** - Pulls latest USD exchange rates from ExchangeRate API
- **Transform** - Cleans and filters data into a structural table
- **Load** - Stores results into a local PostgreSQL database

## Tech Stack

- Python 3
- Pandas
- SQLAlchemy
- PostgreSQL
- ExchangeRate API (free tier)

## Project Structure

etl_exercise/
├── pipeline.py        # main ETL script
├── requirements.txt   # dependencies
├── .env.example       # environment variable template
└── .gitignore         # protects credentials

## Setup

1. Clone this repository
2. Create a virtual environment and activate it
3. Install dependencies:

pip install -r requirements.txt

4. Copy '.env.example' to '.env' and fill in your database credentials
5. Run the pipeline:

python3pipeline.py

## Output

The pipeline loads exchange rates for these currencies into PostgreSQL:
'AUD, EUR, GBP, IDR, JPY, MYR, SGD'