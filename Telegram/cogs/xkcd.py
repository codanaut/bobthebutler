import requests
import json
import time
import random
import inspect
from telegram import Update
import logging
#
# xkcd Commands 
#

async def xkcd(update: Update, context):
    resp = requests.get('http://xkcd.com/info.0.json')

    data = resp.json()
    title = data['title']
    img = data['img']
  
    message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{update.message.chat.username} - ID:{update.message.chat.id} - Bot:{update.message.from_user.is_bot} - Command:/{inspect.stack()[0][3]}"
    logging.info(message_str)
    print(message_str)
    await update.message.reply_text(f"{title}\n{img}")


async def randomxkcd(update: Update, context):
    resp = requests.get('http://xkcd.com/info.0.json')

    data = resp.json()
    newestxkcd = data['num']
    xkcd = random.randint(1,newestxkcd)
    randomurl = 'https://xkcd.com/' + str(xkcd) +'/info.0.json'
    resp2 = requests.get(randomurl)
    data2 = resp2.json()
    title = data2['title']
    img = data2['img']
  
    message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{update.message.chat.username} - ID:{update.message.chat.id} - Bot:{update.message.from_user.is_bot} - Command:/{inspect.stack()[0][3]}"
    logging.info(message_str)
    print(message_str)
    await update.message.reply_text(f"{title}\n{img}")