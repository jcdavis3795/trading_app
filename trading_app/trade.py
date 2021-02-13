import requests, json
from credentials import *

# Headers for calling the api
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': API_SECRET_KEY}


# using your credentials, return account information
def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)

    return json.loads(r.content)


# create an order by specifying these parameters
def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }

    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)

    return json.loads(r.content)


# return your order history
def get_orders():
    r = requests.get(ORDERS_URL, headers=HEADERS)

    return json.loads(r.content)


# some examples of how to create orders with the create_order() func :

# response = create_order("GME", 100, "buy", "market", "gtc")
# response = create_order("AMZN", 10, "buy", "market", "gtc")
# response = create_order("DASH", 20, "buy", "market", "gtc")

response = get_account()
print(response)

