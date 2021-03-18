import time

async def damp_it(message, coin):
  reply = 'Hello {0.author.mention}, they bought {1} ?'.format(message, coin)
  await message.channel.send(reply)
  time.sleep(1)
  await message.channel.send("...")
  time.sleep(1)
  reply = 'DAMP IT'
  await message.channel.send(reply)

async def pamp_it(message, coin):
  reply = 'Hello {0.author.mention}, they sold {1} ?'.format(message, coin)
  await message.channel.send(reply)
  time.sleep(1)
  await message.channel.send("...")
  time.sleep(1)
  reply = 'PAMP IT'
  await message.channel.send(reply)

async def tell_price(message, coin, price):
  price = '{:,.2f}'.format(price)
  reply = 'Hello {0.author.mention}, you want some {1} ?'.format(message, coin)
  await message.channel.send(reply)
  time.sleep(1)
  await message.channel.send("...")
  time.sleep(1)
  reply = '{0} is currently trading at ${1}'.format(coin, price)
  await message.channel.send(reply)

async def coin_not_found(message, coin):
  reply = 'Hello {0.author.mention}, are you fucking with me ? {1} ?! Fuck off.'.format(message, coin)
  await message.channel.send(reply)

async def hello(message):
  reply = 'Hello {0.author.mention}, you called?'.format(message)
  await message.channel.send(reply)