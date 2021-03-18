import chat
import cryptocompare
import discord
import os

from env import TOKEN

client = discord.Client()


def coin_exists(coin):
    all_coins = cryptocompare.get_coin_list(format=True)
    if coin in all_coins:
        return True
    return False


@client.event
async def on_ready():
    print('Bogdanoff is ready.')
    print('He has logged in as {0.user}'.format(client))


@client.event
async def on_message(message):

    # Don't reply to yourself Bognadoff
    if message.author == client.user:
        return

    # Say hello
    if 'bogdanoff' in message.content.lower():
        await chat.hello(message)
        return

    # Detect a ! command
    if message.content.startswith('!'):
        data = message.content.split()
        if len(data) < 2:
            return

        # Setup variables
        command = data[0]
        coin = data[1]

        if not coin_exists(coin):
            await chat.coin_not_found(message, coin)
            return

        if command == '!dump':
            await chat.damp_it(message, coin)

        elif command == '!pump':
            await chat.pamp_it(message, coin)

        elif command == '!price':
            price = cryptocompare.get_price(coin, 'USD')
            await chat.tell_price(message, coin, price[coin]['USD'])

client.run(TOKEN)
