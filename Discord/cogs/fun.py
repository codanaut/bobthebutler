import discord
from discord import activity
from discord.ext import commands
import random
import aiohttp
import json
import time
import logging

#
# Fun Cog
#

class fun(commands.Cog, name="Random Fun Commands"):

    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(name='repeat', aliases=['copy', 'mimic', 'say'])
    async def do_repeat(self, ctx, *, our_input: str):
        """A simple command which repeats our input.
        In rewrite Context is automatically passed to our commands as the first argument after self."""

        print(f"{time.strftime('%m/%d/%y %I:%M%p')} - /{ctx.command} - Server:{ctx.guild} - User:{ctx.author}")
        await ctx.respond(our_input)
    

    # Magic 8Ball
    @commands.slash_command(name='8ball',
                    description="Answers a yes/no question.",
                    brief="Answers from the beyond.",
                    aliases=['ask_universe','ask','eight_ball', 'eightball', '8-ball'],
                    pass_context=True)
    async def ask(self,ctx):
        possible_responses = [
            'That is a resounding no',
            'It is not looking likely',
            'Too hard to tell',
            'It is quite possible',
            'Definitely',
            'Lets find out!',
            'The World may never know...',
            'Fuck Off, im busy',
            'If you pray hard enough anything is possible',
            'yes',
            'nope',
            'thats a nadda',
            'watch your tone with me boy',
            'survey says.... yes',
            'survey says.... no',
            'survey says.... geta life',
            'if you have to ask you dont want to know',
            'God put me on hold, ill be back with you shortly',
        ]
        embed=discord.Embed(color=0x050505)
        embed.set_author(name="Magic 8Ball", icon_url="https://i.imgur.com/c59iVYd.jpeg")
        embed.add_field(name="Universe Says:", value=random.choice(possible_responses), inline=True)
        await ctx.respond(embed=embed)
        
        message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
        logging.info(message_str)
        print(message_str)
       
    # Bored
    @commands.slash_command(name='bored',
                    description="Suggests an activity",
                    brief="Lets find something to do")
    async def bored(self,ctx):
        async with ctx.typing():
            url = 'http://www.boredapi.com/api/activity'
            async with aiohttp.ClientSession() as session:  # Async HTTP request
                raw_response = await session.get(url)
                response = await raw_response.text()
                response = json.loads(response)
                whattodo = response['activity']
                embed=discord.Embed(title=f"{whattodo}", colour=discord.Colour.random())
                await ctx.respond(embed=embed)
                
                message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
                logging.info(message_str)
                print(message_str)


    # Excuses
    @commands.slash_command(name='excuse',description="Random Excuses")
    async def excuse(self,ctx):
        url = 'https://excuser.herokuapp.com/v1/excuse'
        async with aiohttp.ClientSession() as session:  # Async HTTP request
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            excuse = response[0]['excuse']
            embed=discord.Embed(title=f"{excuse}", colour=discord.Colour.random())
            await ctx.respond(embed=embed)
            
            message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
            logging.info(message_str)
            print(message_str)

    # Useless Facts
    @commands.slash_command(name='uselessfact', description="Random Useless Facts")
    async def uselessfact(self,ctx):
        url = 'https://uselessfacts.jsph.pl/random.json?language=en'
        async with aiohttp.ClientSession() as session:  # Async HTTP request
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            data = response['text']
            embed=discord.Embed(title=f"{data}", colour=discord.Colour.random())
            await ctx.respond(embed=embed)
            
            message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
            logging.info(message_str)
            print(message_str)

    #
    #Jokes
    #

    # Joke
    @commands.slash_command(name='joke',
                    description="Random Joke",
                    brief="Lets find something to do")
    async def joke(self,ctx):
        async with ctx.typing():
            url = 'https://v2.jokeapi.dev/joke/Any?type=single'
            async with aiohttp.ClientSession() as session:  # Async HTTP request
                raw_response = await session.get(url)
                response = await raw_response.text()
                response = json.loads(response)
                joke = response['joke']
                category = response['category']
                id = response['id']
                embed=discord.Embed(title=f"{joke}", colour=discord.Colour.random())
                await ctx.respond(embed=embed)
                
                message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
                logging.info(message_str)
                print(message_str)
    

    #
    # Animal Stuffs
    #

    # Cat Fact
    @commands.slash_command(name='catfact',
                    description="Random Cat Fact")
    async def catfact(self,ctx):
        async with ctx.typing():
            url = 'https://catfact.ninja/fact'
            async with aiohttp.ClientSession() as session:  # Async HTTP request
                raw_response = await session.get(url)
                response = await raw_response.text()
                response = json.loads(response)
                fact = response['fact']
                embed=discord.Embed(title=f"{fact}", colour=discord.Colour.random())
                await ctx.respond(embed=embed)
                
                message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
                logging.info(message_str)
                print(message_str)


    # Dog Fact
    @commands.slash_command(name='dogfact',
                    description="Random Dog Fact")
    async def dogfact(self,ctx):
        async with ctx.typing():
            url = 'https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all'
            async with aiohttp.ClientSession() as session:  # Async HTTP request
                raw_response = await session.get(url)
                response = await raw_response.text()
                response = json.loads(response)
                dfact = response
                factCount = len(dfact)
                ranFact = random.randint(1,factCount)
                fact = response[ranFact]['fact']
                embed=discord.Embed(title=f"{fact}", colour=discord.Colour.random())
                await ctx.respond(embed=embed)
                
                message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
                logging.info(message_str)
                print(message_str)

    # Cat Picture
    @commands.slash_command(name='cat',
                    description="Random Cat Picture")
    async def randomcat(self,ctx):
        async with ctx.typing():
            url = 'https://aws.random.cat/meow'
            async with aiohttp.ClientSession() as session:  # Async HTTP request
                raw_response = await session.get(url)
                response = await raw_response.text()
                response = json.loads(response)
                pic = response['file']
                embed=discord.Embed(colour=discord.Colour.random())
                embed.set_image(url=pic)
                await ctx.respond(embed=embed)

                message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
                logging.info(message_str)
                print(message_str)

    # Dog Picture
    @commands.slash_command(name='dog',
                    description="Random Dog Picture")
    async def randomdog(self,ctx):
        async with ctx.typing():
            url = 'https://random.dog/woof.json'
            async with aiohttp.ClientSession() as session:  # Async HTTP request
                raw_response = await session.get(url)
                response = await raw_response.text()
                response = json.loads(response)
                pic = response['url']
                embed=discord.Embed(colour=discord.Colour.random())
                embed.set_image(url=pic)
                await ctx.respond(embed=embed)

                message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
                logging.info(message_str)
                print(message_str)

    # Fox Picture
    @commands.slash_command(name='fox',
                    description="Random Fox Picture")
    async def randomfox(self,ctx):
        async with ctx.typing():
            url = 'https://randomfox.ca/floof/'
            async with aiohttp.ClientSession() as session:  # Async HTTP request
                raw_response = await session.get(url)
                response = await raw_response.text()
                response = json.loads(response)
                pic = response['image']
                embed=discord.Embed(colour=discord.Colour.random())
                embed.set_image(url=pic)
                await ctx.respond(embed=embed)

                message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
                logging.info(message_str)
                print(message_str)

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.

def setup(bot):
   bot.add_cog(fun(bot))