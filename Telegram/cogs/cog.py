import time
import inspect
from telegram import Update
#
# Testing and Examples
#

async def test(update: Update, context):
    
    #update.message.reply_text(update.message.text)
    await update.message.reply_text("Triggered Test")
    print(f"{time.strftime('%m/%d/%y %I:%M%p')} - /{inspect.stack()[0][3]} - {update.message.chat.username}")
