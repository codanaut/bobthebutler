import requests
import json
import time
import random
import inspect
from telegram import Update

#
# xkcd Commands 
#

async def xkcd(update: Update, context):
    resp = requests.get('http://xkcd.com/info.0.json')

    data = resp.json()
    title = data['title']
    img = data['img']
  
    print(f"{time.strftime('%m/%d/%y %I:%M%p')} - /{inspect.stack()[0][3]} - {update.message.chat.username}")
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
  
    print(f"{time.strftime('%m/%d/%y %I:%M%p')} - /{inspect.stack()[0][3]} - {update.message.chat.username}")
    await update.message.reply_text(f"{title}\n{img}")