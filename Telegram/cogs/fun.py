import random
import time
import inspect
import requests
import logging

#
# Fun Commands
#

async def joke(update, context):
    
    url = 'https://v2.jokeapi.dev/joke/Any?type=single'
    resp = requests.get(url)

    data = resp.json()
    joke = data['joke']

    await update.message.reply_text(joke)
    message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{update.message.chat.username} - ID:{update.message.chat.id} - Bot:{update.message.from_user.is_bot} - Command:/{inspect.stack()[0][3]}"
    logging.info(message_str)
    print(message_str)


async def bored(update, context):
    
    url = 'http://www.boredapi.com/api/activity'
    resp = requests.get(url)

    data = resp.json()
    activity = data['activity']
    
    await update.message.reply_text(activity)
    message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{update.message.chat.username} - ID:{update.message.chat.id} - Bot:{update.message.from_user.is_bot} - Command:/{inspect.stack()[0][3]}"
    logging.info(message_str)
    print(message_str)


async def excuse(update, context):
    
    url = 'https://excuser.herokuapp.com/v1/excuse'
    resp = requests.get(url)

    data = resp.json()
    activity = data[0]['excuse']
    
    await update.message.reply_text(activity)
    message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{update.message.chat.username} - ID:{update.message.chat.id} - Bot:{update.message.from_user.is_bot} - Command:/{inspect.stack()[0][3]}"
    logging.info(message_str)
    print(message_str)


async def uselessfact(update, context):
    
    url = 'https://uselessfacts.jsph.pl/random.json?language=en'
    resp = requests.get(url)

    data = resp.json()
    activity = data['text']
    
    await update.message.reply_text(activity)
    message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{update.message.chat.username} - ID:{update.message.chat.id} - Bot:{update.message.from_user.is_bot} - Command:/{inspect.stack()[0][3]}"
    logging.info(message_str)
    print(message_str)

#
# Animals
#

# Cats
async def catfacts(update, context):
    
    url = 'https://catfact.ninja/fact'
    resp = requests.get(url)

    data = resp.json()
    fact = data['fact']
    
    await update.message.reply_text(fact)
    message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{update.message.chat.username} - ID:{update.message.chat.id} - Bot:{update.message.from_user.is_bot} - Command:/{inspect.stack()[0][3]}"
    logging.info(message_str)
    print(message_str)


async def randomcat(update, context):
    
    url = 'https://aws.random.cat/meow'
    resp = requests.get(url)

    data = resp.json()
    catpic = data['file']
    
    await update.message.reply_text(catpic)
    message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{update.message.chat.username} - ID:{update.message.chat.id} - Bot:{update.message.from_user.is_bot} - Command:/{inspect.stack()[0][3]}"
    logging.info(message_str)
    print(message_str)

# Dogs
async def dogfacts(update, context):
    
    url = 'https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all'
    resp = requests.get(url)

    data = resp.json()
    factCount = len(data)
    ranFact = random.randint(1,factCount)
    fact = data[ranFact]['fact']
    
    await update.message.reply_text(fact)
    message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{update.message.chat.username} - ID:{update.message.chat.id} - Bot:{update.message.from_user.is_bot} - Command:/{inspect.stack()[0][3]}"
    logging.info(message_str)
    print(message_str)


async def randomdog(update, context):
    
    url = 'https://random.dog/woof.json'
    resp = requests.get(url)

    data = resp.json()
    pic = data['url']
    
    await update.message.reply_text(pic)
    message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{update.message.chat.username} - ID:{update.message.chat.id} - Bot:{update.message.from_user.is_bot} - Command:/{inspect.stack()[0][3]}"
    logging.info(message_str)
    print(message_str)

# foxes
async def randomfox(update, context):
    
    url = 'https://randomfox.ca/floof/'
    resp = requests.get(url)

    data = resp.json()
    foxpic = data['image']
    
    await update.message.reply_text(foxpic)
    message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{update.message.chat.username} - ID:{update.message.chat.id} - Bot:{update.message.from_user.is_bot} - Command:/{inspect.stack()[0][3]}"
    logging.info(message_str)
    print(message_str)