import requests
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load credentials
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Extract
def extract():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    print ("✅ Data extracted successfully!")
    return data

# Transform
def transform(data):
    base_currency = data["base"]
    date = data["date"]
    rates = data["rates"]

    df = pd.DataFrame(list(rates.items()), columns=["target_currency", "rate"])
    df["base_currency"] = base_currency
    df["date"] = date
    df = df[["date", "base_currency", "target_currency", "rate"]]

    # Filter currencies
    currencies_we_want = ["IDR", "JPY", "EUR", "GBP", "AUD", "SGD", "MYR"]
    df_filtered = df[df["target_currency"].isin(currencies_we_want)].reset_index(drop=True)

    print ("✅ Data transformed successfully!")
    return df_filtered

# Load
def load(df):
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    df.to_sql("exchange_rates", engine, if_exists="append", index=False)
    print ("✅ Data loaded successfully!")
    
# Run Pipeline
if __name__ == "__main__":
    data = extract()
    df = transform(data)
    load(df)
    print("✅ ETL Pipeline executed successfully!")