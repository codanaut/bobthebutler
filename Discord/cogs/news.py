import discord
from discord.ext import commands
import random
import aiohttp
import json
import time

#
# News Cog 
#
# Make sure to change class name in line 13 & 36
# 

class news(commands.Cog, name="News"):

    def __init__(self, bot):
        self.bot = bot

    
    # Top News
    @commands.slash_command(name='topnews', description="Top News Article Right Now")
    async def topnews(self,ctx):

        url = 'https://www.reddit.com/r/news.json'
        headers = {
        'User-Agent': 'web:bobthebutler:v0.1'}
        async with aiohttp.ClientSession() as session:  # Async HTTP request
            raw_response = await session.get(url,headers=headers)
            response = await raw_response.text()
            data = json.loads(response)
            title = data['data']['children'][1]['data']['title']
            articleUrl = data['data']['children'][1]['data']['url']

            print(f"{time.strftime('%m/%d/%y %I:%M%p')} - /{ctx.command} - Server:{ctx.guild} - User:{ctx.author}")
            await ctx.respond(articleUrl)


    # Top World News
    @commands.slash_command(name='topworldnews', description="Top r/world new article")
    async def topworldnews(self,ctx):

        url = 'https://www.reddit.com/r/worldnews.json'
        headers = {
        'User-Agent': 'web:bobthebutler:v0.1'}
        async with aiohttp.ClientSession() as session:  # Async HTTP request
            raw_response = await session.get(url,headers=headers)
            response = await raw_response.text()
            data = json.loads(response)
            title = data['data']['children'][1]['data']['title']
            articleUrl = data['data']['children'][1]['data']['url']

            print(f"{time.strftime('%m/%d/%y %I:%M%p')} - /{ctx.command} - Server:{ctx.guild} - User:{ctx.author}")
            await ctx.respond(articleUrl)


    # Random news and world news
    @commands.slash_command(name='news', description="Random news articles")
    async def news(self,ctx):

        urlWorldNews = "https://www.reddit.com/r/worldnews.json"
        urlNews = "https://www.reddit.com/r/news.json"
        ranNews = random.choice([urlNews,urlWorldNews])
        headers = {
        'User-Agent': 'web:bobthebutler:v0.1'}
        async with aiohttp.ClientSession() as session:  # Async HTTP request
            raw_response = await session.get(ranNews,headers=headers)
            response = await raw_response.text()
            data = json.loads(response)
            ranArticle = random.randint(1,26)
            title = data['data']['children'][ranArticle]['data']['title']
            articleUrl = data['data']['children'][ranArticle]['data']['url']

            print(f"{time.strftime('%m/%d/%y %I:%M%p')} - /{ctx.command} - Server:{ctx.guild} - User:{ctx.author}")
            await ctx.respond(articleUrl)

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.

def setup(bot):
   bot.add_cog(news(bot))