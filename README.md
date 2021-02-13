# trading_app
a simple app that uses the alpaca.markets paper trading API to create orders. The main focus of this project was communicating with the API and familiarizing myself with requests.

This script includes a few functions for basic interfacing with the alpaca API. These functions are:

get_account()
Which will return a lot of your account information like buying power, cash, portfolio value and account id

create_order()
Which will create your order (provided you have the money) and takes the arguments 'symbol, qty, side, type, time_in_force.' An example of how this would look for creating an actual order: 

create_order("DASH", 20, "buy", "market", "gtc")

get_orders()
Which will return your recent order history

I created these functions using the alpaca API documentation.
