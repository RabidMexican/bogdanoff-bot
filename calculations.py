import cryptocompare
import datetime

currency = 'USD'


def get_daily(coin):
    today = cryptocompare.get_historical_price(
        coin,
        currency,
        datetime.datetime.now())[coin][currency]

    yesterday = cryptocompare.get_historical_price(
        coin,
        currency,
        datetime.datetime.now() - datetime.timedelta(days=1))[coin][currency]

    increase = True
    if(today < yesterday):
        increase = False

    diff = today - yesterday
    daily = (diff / today) * 100
    
    return format_percentage(daily, increase)


def format_percentage(percentage, increase):
    result = round(percentage, 2)
    if(increase):
        result = '+' + str(result)
    else:
        result = '-' + str(result)
    return result + '%'
