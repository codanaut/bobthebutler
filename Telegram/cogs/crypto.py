import requests
import json
import time
import inspect
from telegram import Update
import logging
#
# Crypto Commands 
#

async def btc(update: Update, context):
    resp = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')

    data = resp.json()
    xbtusd = data['result']['XXBTZUSD']

    ask = xbtusd['a'][0]
    bid = xbtusd['b'][0]
    low = xbtusd['l'][0]
    high = xbtusd['h'][0]

    currentPrice = "{:,.2f}".format(float(xbtusd['a'][0]))

    message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{update.message.chat.username} - ID:{update.message.chat.id} - Bot:{update.message.from_user.is_bot} - Command:/{inspect.stack()[0][3]}"
    logging.info(message_str)
    print(message_str)
    await update.message.reply_text(f"*BTC*\n${currentPrice}",parse_mode='Markdown')


async def nano(update: Update, context):
    resp = requests.get('https://api.kraken.com/0/public/Ticker?pair=NANOUSD')

    data = resp.json()
    coin = data['result']['NANOUSD']

    ask = coin['a'][0]
    bid = coin['b'][0]
    low = coin['l'][0]
    high = coin['h'][0]

    currentPrice = "{:,.2f}".format(float(coin['a'][0]))

    message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{update.message.chat.username} - ID:{update.message.chat.id} - Bot:{update.message.from_user.is_bot} - Command:/{inspect.stack()[0][3]}"
    logging.info(message_str)
    print(message_str)
    await update.message.reply_text(f"*Nano*\n${currentPrice}",parse_mode='Markdown')


async def eth(update: Update, context):
    resp = requests.get('https://api.kraken.com/0/public/Ticker?pair=ethusd')

    data = resp.json()
    coin = data['result']['XETHZUSD']

    ask = coin['a'][0]
    bid = coin['b'][0]
    low = coin['l'][0]
    high = coin['h'][0]

    currentPrice = "{:,.2f}".format(float(coin['a'][0]))

    message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{update.message.chat.username} - ID:{update.message.chat.id} - Bot:{update.message.from_user.is_bot} - Command:/{inspect.stack()[0][3]}"
    logging.info(message_str)
    print(message_str)
    await update.message.reply_text(f"*ETH*\n${currentPrice}",parse_mode='Markdown')