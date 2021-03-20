import crypto
import datetime
import discord
import env

from messenger import Messenger


class Bogdanoff:

    def __init__(self):
        self.client = discord.Client()

        # Get environment variables
        self.token = env.TOKEN
        self.channel_name = env.CHANNEL_NAME
        self.all_channels = []
        self.channel = None

        # Set-up listeners
        self.on_ready = self.client.event(self.on_ready)
        self.on_message = self.client.event(self.on_message)
        self.on_disconnect = self.client.event(self.on_disconnect)

    def start(self):
        self.client.run(self.token)

    async def execute_command(self, message):
        data = message.content.split()
        command = data[0][1:]

        # Commands with no parameters
        if len(data) < 2:
            if(command.upper() in crypto.get_all_coins()):
                command = command.upper()
                data = crypto.get_crypto(command)
                await self.messenger.crypto2(command, data)

            elif command == 'kill':
                await self.messenger.logout()
                await self.client.close()

            elif command == 'help':
                await self.messenger.help()
            return

        # Commands with a coin
        coin = data[1].upper()
        if not crypto.coin_exists(coin):
            await self.messenger.coin_not_found(coin)
            return

        if command == 'dump':
            await self.messenger.damp_it(coin)

        elif command == 'pump':
            await self.messenger.pamp_it(coin)

        elif command == 'price':
            price = crypto.get_price(coin)
            await self.messenger.tell_price(coin, price)

        elif command == 'daily':
            daily = crypto.get_daily(coin)
            await self.messenger.day(coin, daily)

        elif command == 'info':
            info = crypto.get_info(coin)
            await self.messenger.info(coin, info)

    async def on_message(self, message):
        self.messenger.set_message(message)

        # Don't talk to yourself, Bognadoff
        if message.author == self.client.user:
            return

        # If message in bot channel
        if self.channel_name == str(message.channel):

            if 'bogdanoff' in message.content.lower():
                await self.messenger.hello()

            elif message.content.startswith('!'):
                await self.execute_command(message)

    async def on_disconnect(self):
        print("Bogdanoff has disconnected")

    async def on_ready(self):
        # Set-up messenger
        self.all_channels = self.client.get_all_channels()
        self.channel = discord.utils.get(
            self.all_channels, name=env.CHANNEL_NAME)
        self.messenger = Messenger(self.channel)

        print('Bogdanoff is ready.')
        print('He has logged in as {0.user}'.format(self.client))

        await self.messenger.login()
