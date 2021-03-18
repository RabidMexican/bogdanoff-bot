import messages
import cryptocompare
import discord
import env
import os

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
async def on_message(discord_message):

    # Don't reply to yourself Bognadoff
    if discord_message.author == client.user:
        return

    # Say hello
    if 'bogdanoff' in discord_message.content.lower():
        await messages.hello(discord_message)
        return

    # Detect a ! command
    if discord_message.content.startswith('!'):
        data = discord_message.content.split()
        if len(data) < 2:
            return

        command = data[0]
        coin = data[1].upper()

        if not coin_exists(coin):
            await messages.coin_not_found(discord_message, coin)
            return

        if command == '!dump':
            await messages.damp_it(discord_message, coin)

        elif command == '!pump':
            await messages.pamp_it(discord_message, coin)

        elif command == '!price':
            price = cryptocompare.get_price(coin, 'USD')
            await messages.tell_price(discord_message, coin, price[coin]['USD'])

client.run(env.TOKEN)
