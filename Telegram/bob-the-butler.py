import time
import inspect
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Import Cogs
from cogs.crypto import *
from cogs.xkcd import *
from cogs.cog import *
from cogs.tools import *
from cogs.fun import *
from cogs.news import *


# set token
secret_file = open('token.secret','r')
token = secret_file.readline().rstrip()


# Start Command
async def start(update, context):
    """Send a message when the command /start is issued."""
    print(f"{time.strftime('%m/%d/%y %I:%M%p')} - /{inspect.stack()[0][3]} - {update.message.chat.username}")
    await update.message.reply_text('Welcome!\n/help - to get started')


async def help(update, context):
    """Send a message when the command /help is issued."""
    print(f"{time.strftime('%m/%d/%y %I:%M%p')} - /{inspect.stack()[0][3]} - {update.message.chat.username}")
    await update.message.reply_text(
        'Commands\n'
        '\n'
        'News\n'
        '/news - Random News Article\n'
        '/topnews - Top of r/news\n'
        '/topworldnews - Top of r/worldnews\n'
        '\n'
        'Crypto\n'
        '/btc - Bitcoin\n'
        '/nano - Nano\n'
        '/eth - Eth\n'
        '\n'
        'xkcd\n'
        '/xkcd - xkcd\n'
        '/randomxkcd - random xkcd\n'
        '\n'
        'Fun\n'
        '/joke - get a random joke\n'
        '/bored - activities to do\n'
        '/excuse - random excuse\n'
        '/uselessfact - useless facts\n'
        '\n'
        'Animals\n'
        '/catfacts - facts about cats\n'
        '/randomcat - random cat pic\n'
        '/dogfacts - facts about dogs\n'
        '/randomdog - random dog pic\n'
        '/randomfox - random fox pic\n'
        '\n'
        'Tools\n'
        '/userinfo - username & ID'
        )


async def echo(update: Update, context):
    """Echo the user message."""
    print(f"{time.strftime('%m/%d/%y %I:%M%p')} - /{inspect.stack()[0][3]} - {update.message.chat.username}")
    await update.message.reply_text(update.message.text)


# Buld app
app = ApplicationBuilder().token(token).build()

#
# Register all added commands below!
#

# on different commands - answer in Telegram
app.add_handler(CommandHandler("start", start))
#app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler(['help','commands'], help))
    
#Crypto Commands
app.add_handler(CommandHandler("btc", btc))
app.add_handler(CommandHandler("nano", nano))
app.add_handler(CommandHandler("eth", eth))

#xkcd commands
app.add_handler(CommandHandler("xkcd", xkcd))
app.add_handler(CommandHandler("randomxkcd", randomxkcd))

#Fun Cog
app.add_handler(CommandHandler("joke", joke))
app.add_handler(CommandHandler("bored", bored))
app.add_handler(CommandHandler("excuse", excuse))
app.add_handler(CommandHandler("uselessfact", uselessfact))
app.add_handler(CommandHandler("catfacts", catfacts))
app.add_handler(CommandHandler("randomcat", randomcat))
app.add_handler(CommandHandler("dogfacts", dogfacts))
app.add_handler(CommandHandler("randomdog", randomdog))
app.add_handler(CommandHandler("randomfox", randomfox))

#Tools Cog
app.add_handler(CommandHandler("userinfo", userinfo))

#News Cog
app.add_handler(CommandHandler("topnews", topnews))
app.add_handler(CommandHandler("topworldnews", topworldnews))
app.add_handler(CommandHandler("news", news))

#Testing Commands
app.add_handler(CommandHandler(['test','test2','testytest'], test))

# on noncommand i.e message - echo the message on Telegram
app.add_handler(MessageHandler(filters.TEXT, echo))


# Start the Bot
print("Starting Bot!")
print(time.strftime('%m/%d/%y %I:%M%p'))
app.run_polling()
