import discord
from discord.ext import commands
import time
import openai

#
# Config OpenAI with API Key
# 
secret_file = open('openAI.secret','r')
client_token = secret_file.readline().rstrip()
openai.api_key = client_token

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
        
        content = message.content.replace(f'<@{self.bot.user.id}>', '').strip()

        # If Mentioned in any channel
        if self.bot.user in message.mentions and message.guild: # Check if the bot is mentioned
            if message.author.id != self.bot.user.id:
                async with message.channel.typing():
                    print(f"{time.strftime('%m/%d/%y %I:%M%p')} - @{self.bot.user} - Server:{message.guild} - User:{message.author}")
                    chatReply = chatgpts(content)
                    await message.reply(f'{chatReply}')
                    await self.bot.process_commands(message)
            
            else:
                #print("can't reply to self")
                pass
            
        # if messaged in DM's    
        if not message.guild:
            if message.author.id != self.bot.user.id:
                async with message.channel.typing():
                    print(f"{time.strftime('%m/%d/%y %I:%M%p')} - @{self.bot.user} - Server:{message.guild} - User:{message.author}")
                    chatReply = chatgpts(content)
                    await message.reply(f'{chatReply}')
                    await self.bot.process_commands(message)
                
            else:
                #print("can't reply to self")
                pass
        else:
            pass

    # catches and hides errors or prints for testing
    @commands.Cog.listener()
    async def on_command_error(ctx,message,error):
        #print(f"Error: {error}")
        pass
            

    @commands.slash_command(name="chat",description="ChatGPT")
    async def chat(self, ctx,*, question: str):
        print(f"{time.strftime('%m/%d/%y %I:%M%p')} - /{ctx.command} - Server:{ctx.guild} - User:{ctx.author}")
        chatReply = chatgpts(question)
        await ctx.respond(chatReply)

    

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.

def setup(bot):
   bot.add_cog(chatgpt(bot))


def chatgpts(question):
    user_input = question

    # Create ChatCompletion with user input
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=1000,
        stop=None,
        messages=[
            {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible."},
            {"role": "user", "content": user_input}
        ]
    )

    # Print Response
    print("--")
    print(f"User:\n{user_input}")
    print(f"{completion.choices[0].message.role}:\n{completion.choices[0].message.content}")
    print("--")
    answer = completion.choices[0].message.content
    return answer
