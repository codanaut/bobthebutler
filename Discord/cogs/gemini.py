import discord
from discord.ext import commands
import time
import google.generativeai as genai
import logging
import os

#
# Config geminiAI.secret with API Key - https://makersuite.google.com/app/apikey
# 

# Set Token
# Attempt to get the environment variable 'CLIENT_TOKEN'
client_token = os.getenv('gemini')

if not client_token:
    # Environment variable not set, attempt to read from file as a fallback
    try:
        with open('geminiAI.secret', 'r') as secret_file:
            client_token = secret_file.readline().rstrip()
            if not client_token:
                # File is empty
                print("Gemini: No token configured")
                exit()
            else:
                print("Gemini: Token Set from file!")
    except FileNotFoundError:
        # File does not exist
        print("Gemini: No token configured and secret file not found")
        exit()
else:
    # Environment variable is set, proceed with using the client_token
    print("Gemini: Token Set from environment variable!")

client = genai.configure(api_key=client_token)

#
# ChatGPT Cog 
#
# Make sure to change class name in line 19, 34, 71
# 

class chatgpt(commands.Cog):
    

    def __init__(self, bot):
        self.bot = bot
        self.conversation_history = {}

    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bard Loaded & Ready')
        print("------------")
        #print('Logged in as ---->', self.bot.user)
        #print('ID:', self.bot.user.id)

    @commands.Cog.listener('on_message')
    async def my_on_message(self, message):
        if message.author.bot:  # Check if the author is a bot
            return
        
        content = message.content.replace(f'<@{self.bot.user.id}>', '').strip()

        # If Mentioned in any channel
        if self.bot.user in message.mentions and message.guild: # Check if the bot is mentioned
            if message.author.id != self.bot.user.id:
                await message.channel.trigger_typing()
                
                # Get or initialize the conversation history
                history_key = message.author.id  # Use author ID as the history key
                history = self.conversation_history.get(history_key, [])

                # Generate reply and update history
                chatReply, updated_history = aiChat(content, history)
                self.conversation_history[history_key] = updated_history
                
                await message.reply(f'{chatReply}')
                await self.bot.process_commands(message)
                message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{message.author} - Server: {message.guild} - Message: {message.content} "
                logging.info(message_str)
                print(message_str)
            else:
                #print("can't reply to self")
                pass
            
        # if messaged in DM's    
        if not message.guild:
            if message.author.id != self.bot.user.id:
                await message.channel.trigger_typing()
                
                # Get or initialize the conversation history
                history_key = message.author.id  # Use author ID as the history key
                history = self.conversation_history.get(history_key, [])

                # Generate reply and update history
                chatReply, updated_history = aiChat(content, history)
                self.conversation_history[history_key] = updated_history

                await message.channel.send(f'{chatReply}')
                await self.bot.process_commands(message)
                message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{message.author} - Server: DM - Message: {message.content} "
                logging.info(message_str)
                print(message_str)
            else:
                #print("can't reply to self")
                pass
        else:
            pass


    # catches and hides errors or prints for testing
    @commands.Cog.listener()
    async def on_command_error(ctx,message,error):
        print(f"Error: {error}")
        message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - Error: {error} "
        logging.info(message_str)
        pass
            
    # Slash Chat Command Command
    @commands.slash_command(name="gemini",description="Google's Gemini Pro AI")
    async def chat(self, ctx, question: discord.Option(str)):
        await ctx.trigger_typing()
        await ctx.defer()
        
        # Get or initialize the conversation history
        history_key = ctx.author.id  # Use author ID as the history key
        history = self.conversation_history.get(history_key, [])

                # Generate reply and update history
        chatReply, updated_history = aiChat(question, history)
        self.conversation_history[history_key] = updated_history

        await ctx.respond(chatReply)
        message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
        logging.info(message_str)
        print(message_str)
    
    # Slash Command - Reset Chat
    @commands.slash_command(name="clearchat",description="Clear Chat Convo with Bard")
    async def resetConversation(self, ctx):
        await ctx.trigger_typing()
        
        # Use user or channel ID as the key, depending on context
        history_key = ctx.author.id

        # Check if the user/channel has a conversation history and reset it
        if history_key in self.conversation_history:
            self.conversation_history[history_key] = []
            await ctx.respond("Your conversation history has been reset.")
        else:
            await ctx.respond("No conversation history to reset.")
        message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
        logging.info(message_str)
        print(message_str)

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.

def setup(bot):
   bot.add_cog(chatgpt(bot))



def aiChat(question, history):
    user_input = question

    # Set up the model
    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    },
    ]

    model = genai.GenerativeModel(model_name="gemini-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)
    
    initial_convo_setup = [
        {
            "role": "user",
            "parts": ["You are Bob the butler, a helpful discord bot trained on Gemini Pro. Answer as concisely as possible."]
        },
        {
            "role": "model",
            "parts": ["Greetings, I am Bob the butler bot, powered by the Gemini Pro training model. I am here to assist you in any way I can. Please let me know how I may be of service."]
        },
    ]

    if not history:
        history = initial_convo_setup.copy()
    
    convo = model.start_chat(history=history)    
    convo.send_message(user_input)
    answer = convo.last.text

    # Update history with the new interaction
    new_history = history + [
        {"role": "user", "parts": [user_input]},
        {"role": "model", "parts": [answer]}
    ]

    print("--")
    print(f"User: {user_input}")
    print(convo.last.text)
    print("--")
    return answer, new_history