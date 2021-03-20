import discord
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

    async def send_embed(self, title, url, desc):
        embed = discord.Embed(
            title=title,
            url='https://cryptocompare.com' + url,
            description=desc
        )
        await self.channel.send(embed=embed)
        time.sleep(1)

    # MESSAGES

    async def coin_not_found(self, coin):
        await self.send_message('Are you fucking with me ? {1} ?!'.format(self.message, coin))

    async def damp_it(self, coin):
        await self.send_message('Hello {0.author.mention}, they bought the {1} ?'.format(self.message, coin))
        await self.send_message('. . .')
        await self.send_message(':chart_with_downwards_trend:\t DAMP IT \t:chart_with_downwards_trend:')

    async def day(self, coin, daily):
        await self.send_message('How is {0} doing today?'.format(coin))
        await self.send_message('{0} is {1} today'.format(coin, daily))

    async def hello(self):
        await self.send_message('You called?')

    async def help(self):
        await self.send_message('Ah, need some help ?')
        await self.send_message('Here are the available commands : ')
        await self.send_message("""```
            +---------------+----------------------------+
            | !help         | Get a list of commands     |
            +---------------+----------------------------+
            | !info {coin}  | Get info about a coin      |
            +---------------+----------------------------+
            | !price {coin} | Get the price of a coin    |
            +---------------+----------------------------+
            | !daily {coin} | Get daily change of a coin |
            +---------------+----------------------------+
            | !dump {coin}  | Dump a coin                |
            +---------------+----------------------------+
            | !pump {coin}  | Pump a coin                |
            +---------------+----------------------------+
            | !kill         | Kill Bognadoff             |
            +---------------+----------------------------+
            ```""")

    async def info(self, coin, info):
        await self.send_message('Here is some information for {0} . . .'.format(coin))
        await self.send_embed(info['FullName'], info['Url'], info['Description'])

    async def login(self):
        await self.send_message('Do not worry everyone, I have arrived!')

    async def logout(self):
        await self.send_message('I am leaving! Check out https://github.com/RabidMexican/bogdanoff-bot and host me !')

    async def pamp_it(self, coin):
        await self.send_message('Hello {0.author.mention}, they sold the {1} ?'.format(self.message, coin))
        await self.send_message('. . .')
        await self.send_message(':chart_with_upwards_trend:\t PAMP IT \t:chart_with_upwards_trend:')

    async def tell_price(self, coin, price):
        await self.send_message('Hello {0.author.mention}, you want some {1} ?'.format(self.message, coin))
        await self.send_message('. . .')
        await self.send_message('{0} is currently trading at {1}'.format(coin, price))
