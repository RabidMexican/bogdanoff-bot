import time


async def damp_it(message, coin):
    await send_message(message, 'Hello {0.author.mention}, they bought {1} ?'.format(message, coin))
    await send_message(message, "...")
    await send_message(message, 'DAMP IT')


async def pamp_it(message, coin):
    await send_message(message, 'Hello {0.author.mention}, they sold {1} ?'.format(message, coin))
    await send_message(message, "...")
    await send_message(message, 'PAMP IT')


async def tell_price(message, coin, price):
    price = '{:,.2f}'.format(price)
    await send_message(message, 'Hello {0.author.mention}, you want some {1} ?'.format(message, coin))
    await send_message(message, "...")
    await send_message(message, '{0} is currently trading at ${1}'.format(coin, price))


async def coin_not_found(message, coin):
    await send_message(message, 'Are you fucking with me ? {1} ?!'.format(message, coin))


async def hello(message):
    await send_message(message, 'You called?'.format(message))


async def send_message(message, reply):
    await message.channel.send(reply)
    time.sleep(1)
