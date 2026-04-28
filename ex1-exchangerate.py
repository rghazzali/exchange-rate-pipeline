import requests

# Ask for input
from_currency = input("Enter currency code to convert from (e.g. USD, JPY, EUR):")
to_currency = input("Enter currency code to convert to (e.g. IDR, GBP, AUD):")
if to_currency == "":
    to_currency = "IDR"

# Ask for amount
amount_input = input("Enter amount (default: 1): ")
if amount_input == "":
    amount = 1
else:
    amount = float(amount_input)

# Hit the API
url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
response = requests.get(url)
data = response.json()

# Make the GET request
rate = data["rates"][to_currency]
date = data["date"]
result = rate * amount

# Format amount
if amount >= 1:
    formatted_amount = f"{amount:,.2f}"
else:
    formatted_amount = f"{amount:.6f}"

# Format result
if result >= 1:
    formatted_result = f"{result:,.2f}"
else:
    formatted_result = f"{result:.6f}"

# Format rate
if rate >= 1:
    formatted_rate = f"{rate:,.2f}"
else:
    formatted_rate = f"{rate:.6f}"

# Print the results
print(f"\nDate: {date}")
print(f" {formatted_amount} {from_currency} = {formatted_result} {to_currency}")