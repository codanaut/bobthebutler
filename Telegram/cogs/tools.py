import inspect
import time

#
# Tools
#

async def userinfo(update, context):

    username = update.message.chat.username
    userID = update.message.chat.id
    #print(update.message.chat)
    print(f"{time.strftime('%m/%d/%y %I:%M%p')} - /{inspect.stack()[0][3]} - {update.message.chat.username}")
    await update.message.reply_text(f"Username: {username}\nUser ID: {userID}")