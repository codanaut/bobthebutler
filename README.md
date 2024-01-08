# Bob The Butler
A general purpose / fun bot for Discord &amp; Telegram.

All features are kept the same between both the discord and the telegram version. The only big difference being telegram does not have a radio module. 

---

# Discord

The discord version of Bob The Butler. Works in servers and dm's. You will need to generate a bot token from the Discord Developer Portal to run your own version. 

## Self Host

Once cloned you will need to create a token file called `token.secret` inside the discord folder and place your bots token in that file.

You also need to create `geminiAI.secret` for the geminiAI to work. Same with `openAI.secret` if you want to use chatgpt instead. 

### Docker

This is the easiest and suggested method for hosting.

**Build**

     docker build -t bob_discord .

**Run**

     sudo docker run -d --name bob_discord -it bob_discord:latest

---

### Manual Install:

To run Bob outside of docker you will need `python 3.10`. Currently 3.11,3.12 arn't working with pycord.

**Install PyCord**

We are now using [PyCord](https://github.com/Pycord-Development/pycord) instead of Discord.py for slash command support. If you don't want radio support you can install without the "[voice]"

    python3 -m pip install -U "py-cord[voice]"

(Also requires `FFMPEG` for the radio module if you want to use it. The radio module is not being kept up right now! Check out my project `RadioCord` instead!)

**Install the rest of the Requirements**

     pip install -r requirements.txt

This will install both `openai` and `google-generativeai` libraries for ChatGPT & Gemini.

**Run BobTheButler**

Make sure you've added the `token.secret` file and then run the program.

     python bobthebutler.py




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


## ChatGPT Module

If you want to use the chatgpt module, you will need to create an api key. 

This requires an OpenAI subscription as it uses the chatgpt 3.5-turbo API.

Create a token file called `openAI.secret` inside the discord/telegram folder and place your OpenAI token in that file.

Finally, enable the chatgpt module inside the main bobthebutler.py file. This is disabled by default to use Gemini's free api instead.


## Gemini Module

If you want to use the Gemini module, you will need to create an api key. 

This is free through the [Google AI Studio](https://makersuite.google.com/app/apikey)

Create a token file called `geminiAI.secret` inside the discord/telegram folder and place your api token in that file.

This module is enabled by default for Bob Discord to provide free AI to the chat. Will be enabled on Telegram later also. 