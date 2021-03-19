# bogdanoff-bot
The Bogdanoff Discord chat-bot.

## Setup

Create a file named env.py using the env.py.example file template provided.

Inside env.py you can define the following environment variables:

| Variable        | Description                        | 
|:---------------:|:----------------------------------:|
| TOKEN           | Discord bot token                  |
| CHANNEL_NAME    | Bot channel name                   |
| CURRENCY        | Price currency                     |
| CURRENCY_SYMBOL | Symbol for chosen currency         |
| EXCHANGE        | Exchange to use for calculations   |

Next we need to install the discord and cryptocompare packages using pip :
```
pip install discord cryptocompare
```

Now we can run the bot :
```
python main.py
```

## Commands

You can use the following commands, if a cryptocurrency is not found, Bogdanoff will let you know.

```
!help
```
```
!kill
```
```
!dump BTC
```
```
!pump BTC
```
```
!price BTC
```
```
!daily BTC
```
