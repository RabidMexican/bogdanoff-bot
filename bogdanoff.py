import cryptocompare
import discord
import env
import os

from messenger import Messenger


class Bogdanoff:

    def __init__(self):
        self.client = discord.Client()

        self.token = env.TOKEN
        self.channel_name = env.CHANNEL_NAME

        # setup listeners
        self.on_ready = self.client.event(self.on_ready)
        self.on_message = self.client.event(self.on_message)

    def start(self):
        self.client.run(self.token)

    def get_command(self, message):
        data = message.content.split()
        if len(data) < 2:
            return None
        return data

    def coin_exists(self, coin):
        all_coins = cryptocompare.get_coin_list(format=True)
        if coin in all_coins:
            return True
        return False

    async def execute_command(self, message):
        data = self.get_command(message)
        command = data[0]
        coin = data[1].upper()

        if not self.coin_exists(coin):
            await messages.coin_not_found(coin)
            return

        if command == '!dump':
            await self.messenger.damp_it(coin)

        elif command == '!pump':
            await self.messenger.pamp_it(coin)

        elif command == '!price':
            price = cryptocompare.get_price(coin, 'USD')
            await self.messenger.tell_price(coin, price[coin]['USD'])

    async def on_message(self, message):
        self.messenger.set_message(message)

        # Don't talk to yourself, Bognadoff
        if message.author == self.client.user:
            return

        # Say hello
        if 'bogdanoff' in message.content.lower():
            await self.messenger.hello()

        # If message in bot channel
        elif self.channel_name == str(message.channel):
            # Detect a ! command
            if message.content.startswith('!'):
                await self.execute_command(message)

    async def on_ready(self):
        all_channels = self.client.get_all_channels()
        my_channel = discord.utils.get(all_channels, name=env.CHANNEL_NAME)
        self.messenger = Messenger(my_channel)

        print('Bogdanoff is ready.')
        print('He has logged in as {0.user}'.format(self.client))

        await self.messenger.login()
