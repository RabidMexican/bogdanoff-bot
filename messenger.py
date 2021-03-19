import time


class Messenger:

    def __init__(self, channel):
        self.channel = channel
        self.message = 'Hello, I am Bodnadoff'

    def set_channel(self, channel):
        self.channel = channel

    def set_message(self, message):
        self.message = message

     # Send a message
    async def send_message(self, reply):
        await self.channel.send(reply)
        time.sleep(1)

    # MESSAGES

    async def coin_not_found(coin):
        await self.send_message(message, 'Are you fucking with me ? {1} ?!'.format(self.message, coin))

    async def damp_it(self, coin):
        await self.send_message('Hello {0.author.mention}, they bought {1} ?'.format(self.message, coin))
        await self.send_message('...')
        await self.send_message('DAMP IT')

    async def hello(self):
        await self.send_message('You called?')

    async def login(self):
        await self.send_message('Do not worry everyone, I have arrived!')

    async def logout(self):
        await self.send_message('I am leaving! Check out https://github.com/RabidMexican/bogdanoff-bot and host me !')

    async def pamp_it(self, coin):
        await self.send_message('Hello {0.author.mention}, they sold {1} ?'.format(self.message, coin))
        await self.send_message('...')
        await self.send_message('PAMP IT')

    async def tell_price(self, coin, price):
        price = '{:,.2f}'.format(price)
        await self.send_message('Hello {0.author.mention}, you want some {1} ?'.format(self.message, coin))
        await self.send_message('...')
        await self.send_message('{0} is currently trading at ${1}'.format(coin, price))
