import inspect
import time
import logging
#
# Tools
#

async def userinfo(update, context):

    username = update.message.chat.username
    userID = update.message.chat.id
    #print(update.message.chat)
    message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{update.message.chat.username} - ID:{update.message.chat.id} - Bot:{update.message.from_user.is_bot} - Command:/{inspect.stack()[0][3]}"
    logging.info(message_str)
    print(message_str)
    await update.message.reply_text(f"Username: {username}\nUser ID: {userID}")