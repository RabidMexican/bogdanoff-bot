import cryptocompare
import datetime

currency = 'USD'
currency_symbol = '$'
exchange = 'Kraken'


def get_all_coins():
    return cryptocompare.get_coin_list(format=True)


def get_daily(coin):
    data = cryptocompare.get_avg('BTC', currency=currency, exchange=exchange)
    return format_percentage(data['CHANGEPCT24HOUR'])


def get_price(coin):
    price = cryptocompare.get_price(coin, currency)
    price = price[coin][currency]


def format_percentage(percentage):
    result = round(percentage, 2)
    if(result > 0):
        result = '+' + str(result)
    return str(result) + '%'


def format_price(price):
    price = round(price, 2)
    return currency_symbol + str(price)
