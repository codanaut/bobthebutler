import requests
import json
import time
import inspect
import random
import logging


async def topnews(update, context):
    url = "https://www.reddit.com/r/news.json"

    headers = {
        'User-Agent': 'web:pydashboard:v0.1 (by /u/BullshitBaron)'
    }

    response = requests.request("GET", url, headers=headers)
    data = response.json()
    title = data['data']['children'][0]['data']['title']
    articleUrl = data['data']['children'][0]['data']['url']
    
    await update.message.reply_text(f"{title}\n{articleUrl}")
    message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{update.message.chat.username} - ID:{update.message.chat.id} - Bot:{update.message.from_user.is_bot} - Command:/{inspect.stack()[0][3]}"
    logging.info(message_str)
    print(message_str)


async def topworldnews(update, context):
    url = "https://www.reddit.com/r/worldnews.json"

    headers = {
        'User-Agent': 'web:pydashboard:v0.1 (by /u/BullshitBaron)'
    }

    response = requests.request("GET", url, headers=headers)
    data = response.json()
    title = data['data']['children'][1]['data']['title']
    articleUrl = data['data']['children'][1]['data']['url']
    
    await update.message.reply_text(f"{title}\n{articleUrl}")
    message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{update.message.chat.username} - ID:{update.message.chat.id} - Bot:{update.message.from_user.is_bot} - Command:/{inspect.stack()[0][3]}"
    logging.info(message_str)
    print(message_str)


async def news(update, context):
    urlWorldNews = "https://www.reddit.com/r/worldnews.json"
    urlNews = "https://www.reddit.com/r/news.json"
    ranNews = random.choice([urlNews,urlWorldNews])

    headers = {
        'User-Agent': 'web:pydashboard:v0.1 (by /u/BullshitBaron)'
    }

    response = requests.request("GET", ranNews, headers=headers)
    data = response.json()
    ranArticle = random.randint(1,26)
    title = data['data']['children'][ranArticle]['data']['title']
    articleUrl = data['data']['children'][ranArticle]['data']['url']
    
    await update.message.reply_text(f"{title}\n{articleUrl}")
    message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{update.message.chat.username} - ID:{update.message.chat.id} - Bot:{update.message.from_user.is_bot} - Command:/{inspect.stack()[0][3]}"
    logging.info(message_str)
    print(message_str)