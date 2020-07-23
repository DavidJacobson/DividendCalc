## Quick program for modeling anual dividend income based on a defined portfolio
# Naive approach - get cash div on last (payout x 4) * # of shares
# Works well enough to give rough idea


# Need iex cloud API token
import requests

DEBUG = False
API_TOKEN = "" # Get API key from iex cloud

prefix = "cloud" if not DEBUG else "sandbox"

# Define portfolio as a dict, ticker -> number of shares
portfolio = \
    {
        'SPY': 100,
        'NOK': 100,
    }


total_return = 0
for symbol in portfolio:
    quantity = portfolio[symbol]
    url = "https://{}.iexapis.com/stable/stock/{}/dividends/ytd?token={}".format(prefix, symbol, API_TOKEN)
    div = float(requests.get(url).json()[0]['amount'])
    total_return += (div * 4) * quantity

total_return = round(total_return, 2) # bc $100.0123123123213 is not useful
print("[*] - Total cash dividend (estimated) over a 1 year period = ${}".format(total_return))
