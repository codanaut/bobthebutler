import discord
from discord.ext import commands
import time
from openai import OpenAI
import logging
#
# Config OpenAI with API Key
# 
secret_file = open('openAI.secret','r')
client_token = secret_file.readline().rstrip()
client = OpenAI(api_key=client_token)
#
# ChatGPT Cog 
#
# Make sure to change class name in line 19, 34, 71
# 

class chatgpt(commands.Cog):
    

    def __init__(self, bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_ready(self):
        print('GPT Loaded & Ready')
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
                #print(f"{time.strftime('%m/%d/%y %I:%M%p')} - @{self.bot.user} - Server:{message.guild} - User:{message.author}")
                chatReply = chatgpts(content)
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
                chatReply = chatgpts(content)
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
        pass
            

    @commands.slash_command(name="chat",description="ChatGPT")
    async def chat(self, ctx, question: discord.Option(str), systemprompt:discord.Option(str, description="Custom Server Prompt", required=False, default=None)):
        await ctx.trigger_typing()
        chatReply = chatgpts(question, systemprompt)
        await ctx.respond(chatReply)
        message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
        logging.info(message_str)
        print(message_str)
    

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.

def setup(bot):
   bot.add_cog(chatgpt(bot))


def chatgpts(question, systemPromt=None):
    user_input = question

    if systemPromt is None:
        # set default value for testarg2
        #systemPromt = "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible."
        systemPromt = "You are Bob the butler, a helpful discord bot trained on ChatGPT. Answer as concisely as possible."

    # Create ChatCompletion with user input
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
    max_tokens=1000,
    stop=None,
    messages=[
        {"role": "system", "content": systemPromt},
        {"role": "user", "content": user_input}
    ])

    # Print Response
    print("--")
    print(f"User: {user_input}")
    print(f"System Prompt: {systemPromt}")
    print(f"{completion.choices[0].message.role}: {completion.choices[0].message.content}")
    print("--")
    answer = completion.choices[0].message.content
    return answer
