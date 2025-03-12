import os
import requests
import json

API_KEY = os.environ.get('MARKETSTACK_KEY')
BASE_URL = 'http://api.marketstack.com/v1/'

# def get_stock_price(stock_symbol):
#     params = {
#         'access_key': API_KEY
#     }   
#     # end_point = ''.join([BASE_URL, "tickers/", stock_symbol, "/intraday/latest"])
#     end_point = ''.join([BASE_URL, "tickers/", stock_symbol, "/eod/latest"])

#     api_result = requests.get(end_point, params)
#     json_result = json.loads(api_result.text)
#     return {
#         "last_price": json_result.get("data", [{}])[0].get("last", "N/A")  # Prevents KeyError
#     }
# 

# def get_stock_price(stock_symbol):
#     params = {
#         'access_key': API_KEY
#     }

#     # Using EOD endpoint
#     end_point = ''.join([BASE_URL, "tickers/", stock_symbol, "/eod/latest"])
#     api_result = requests.get(end_point, params)
#     json_result = json.loads(api_result.text)

#     # Extract "close" price from the response
#     return {
#         "last_price": json_result.get("data", [{}])[0].get("close", "N/A")  # Get "close" price instead
#     }

# result = get_stock_price("AAPL")
# print(f"Stock Price Data: {result}")  # Ensure you see the output



def get_stock_price(stock_symbol):
    params = {
        'access_key': API_KEY
    }

    # Use the EOD endpoint
    end_point = ''.join([BASE_URL, "tickers/", stock_symbol, "/eod/latest"])

    api_result = requests.get(end_point, params)

    print(f"HTTP Status Code: {api_result.status_code}")  # Print response status code
    print(f"Raw Response: {api_result.text}")  # Print full API response

    json_result = json.loads(api_result.text)

    # Extract "close" price directly from the root response
    return {
        "last_price": json_result.get("close", "N/A")  # No need to access "data"
    }

# Run the function
result = get_stock_price("AAPL")
print(f"Stock Price Data: {result}")  # Ensure you see the output


