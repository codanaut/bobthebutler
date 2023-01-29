import requests
import json
import time
import inspect
import random



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
    print(f"{time.strftime('%m/%d/%y %I:%M%p')} - /{inspect.stack()[0][3]} - {update.message.chat.username}")


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
    print(f"{time.strftime('%m/%d/%y %I:%M%p')} - /{inspect.stack()[0][3]} - {update.message.chat.username}")


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
    print(f"{time.strftime('%m/%d/%y %I:%M%p')} - /{inspect.stack()[0][3]} - {update.message.chat.username}")