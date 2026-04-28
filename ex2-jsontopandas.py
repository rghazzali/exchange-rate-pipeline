import requests
import pandas as pd

'''
If we don't know about the data we have to check first
#To check the data structure

print(type(data))
print(data.keys())
print(json.dumps(data, indent=2 ))
'''

# Hit the API
url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
data = response.json()

# Extract rates
base_currency = data["base"]
date = data["date"]
rates = data["rates"]

# Convert rates to DF
df = pd.DataFrame(list(rates.items()), columns=["target_currency", "rate"])

# Add the base as Column
df["base_currency"] = base_currency
df["date"] = date

# Reorder Columns
df = df[["date", "base_currency", "target_currency", "rate"]]

# Print first 10 rows
print(df.head(10))

# Filter currencies
currencies_we_want = ["IDR", "JPY", "EUR", "GBP", "AUD", "SGD", "MYR"]
df_filtered = df[df["target_currency"].isin(currencies_we_want)]

# Reset index
df_filtered = df_filtered.reset_index(drop=True)

# Force to show all Col
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

print(df_filtered)