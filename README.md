# Bob The Butler
A general purpose / fun bot for Discord &amp; Telegram.

All features are kept the same between both the discord and the telegram version. The only big difference being telegram does not have a radio module. 

---

# Discord

The discord version of Bob The Butler. Works in servers and dm's. 

## Install

Once cloned you will need to create a token file called `token.secret` inside the discord folder and place your bots token in that file.

### Requirements:
We are now using [PyCord](https://github.com/Pycord-Development/pycord) instead of Discord.py for slash command support. If you don't want radio support you can install without the "[voice]"

    python3 -m pip install -U "py-cord[voice]"

Also requires `FFMPEG` for the radio module. 


---

# Telegram

The telegram version of Bob The Butler. 

You will need to setup a new bot with BotFather in telegram to generate a token. Then create a token file called `token.secret` inside the telegram folder and place your bots token in that file.

## Install
Install the python package

    pip install python-telegram-bot --upgrade


## Usage
    /commands
Using the /commands command will return a list of all commands. 

If you want commands to show up in a list inside telegram when typing "/" you will need to edit your bot through BotFather and register the commands you want to show up by default. (all commands are still usable even if not registed with botfather)


## ChatGPT Module (Requires OpenAI Subscription)

If you want to use the chatgpt module, you will need to install the OpenAI API.

    pip install openai

This requires an OpenAI subscription as it uses the chatgpt 3.5-turbo API.

Create a token file called `openAI.secret` inside the discord/telegram folder and place your OpenAI token in that file.