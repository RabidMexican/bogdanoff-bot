import cryptocompare
import datetime
import env
import os

# Set-up environment variables
currency = env.CURRENCY
currency_symbol = env.CURRENCY_SYMBOL
exchange = env.EXCHANGE


def get_all_coins(format=True):
    return cryptocompare.get_coin_list(format=format)

def get_crypto(coin):
    data = cryptocompare.get_avg(coin, currency=currency, exchange=exchange)
    return data

def get_daily(coin):
    data = cryptocompare.get_avg(coin, currency=currency, exchange=exchange)
    return format_percentage(data['CHANGEPCT24HOUR'])

def get_info(coin):
    all_coins = get_all_coins(False)
    return all_coins[coin]


def get_price(coin):
    price = cryptocompare.get_price(coin, currency)
    price = price[coin][currency]
    return format_price(price)

def coin_exists(coin):
    all_coins = get_all_coins()
    if coin in all_coins:
        return True
    return False


def format_percentage(percentage):
    result = round(percentage, 2)
    if(result > 0):
        result = '+' + str(result)
    return str(result) + '%'


def format_price(price):
    price = round(price, 2)
    price = '{:,.2f}'.format(price)
    return currency_symbol + str(price)
