import time
import inspect
from telegram import Update
import logging
#
# Testing and Examples
#

async def test(update: Update, context):
    
    #update.message.reply_text(update.message.text)
    await update.message.reply_text("Triggered Test")
    message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{update.message.chat.username} - ID:{update.message.chat.id} - Bot:{update.message.from_user.is_bot} - Command:/{inspect.stack()[0][3]}"
    logging.info(message_str)
    print(message_str)
