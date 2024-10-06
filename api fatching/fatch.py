


import requests
import json

# API URL for cryptocurrency prices
url = "https://api.coingecko.com/api/v3/simple/price"

# Parameters for the API request
params = {
    'ids': 'bitcoin,ethereum,cardano',  # cryptocurrencies to fetch
    'vs_currencies': 'usd'  # target currency
}

def fetch_crypto_data():
    try:
        # Sending a GET request to the API
        response = requests.get(url, params=params)

        # Raise an exception if the status code is not 200 (OK)
        response.raise_for_status()

        # Parse the JSON response
        crypto_data = response.json()

        # Display the data in a formatted manner
        print("Cryptocurrency Prices (USD):")
        print("-" * 30)
        for crypto, details in crypto_data.items():
            print(f"{crypto.capitalize()}: ${details['usd']}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Call the function to fetch and display data
fetch_crypto_data()
