import discord
from discord.ext import commands
import random
import aiohttp
import json
import time
#
# XKCD Cog
#

class xkcd(commands.Cog, name="XKCD Commands"):
    """XkCD Commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='xkcd', description="Latest XKCD", brief="Get Current XKCD")
    async def xkcd(self,ctx):
        async with ctx.typing():
            """Get Current XKCD"""
            url = 'http://xkcd.com/info.0.json'
            async with aiohttp.ClientSession() as session:  # Async HTTP request
                raw_response = await session.get(url)
                response = await raw_response.text()
                response = json.loads(response)
                title = response['title']
                img = response['img']
                embed = discord.Embed(description=title, colour=discord.Colour.blue())
                embed.set_image(url=img)
                print(f"{time.strftime('%m/%d/%y %I:%M%p')} - /{ctx.command} - Server:{ctx.guild} - User:{ctx.author}")
                await ctx.respond(embed=embed)

    # Random xkcd
    @commands.slash_command(name='randomxkcd', description="Random XKCD", brief="Get Random XKCD")
    async def randomxkcd(self,ctx):
        async with ctx.typing():
            """Get Random XKCD"""
            url = 'http://xkcd.com/info.0.json'
            async with aiohttp.ClientSession() as session:  # Async HTTP request
                rraw_response = await session.get(url)
                response = await rraw_response.text()
                response = json.loads(response)
                newestxkcd = response['num']
                xkcd = random.randint(1,newestxkcd)
                randomurl = 'https://xkcd.com/' + str(xkcd) +'/info.0.json'
                raw_response2 = await session.get(randomurl)
                response2 = await raw_response2.text()
                response2 = json.loads(response2)
                title = response2['title'] + " #" + str(xkcd)
                img = response2['img']
                embed = discord.Embed(description=title, colour=discord.Colour.blue())
                embed.set_image(url=img)
                print(f"{time.strftime('%m/%d/%y %I:%M%p')} - /{ctx.command} - Server:{ctx.guild} - User:{ctx.author}")
                await ctx.respond(embed=embed)

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.


def setup(bot):
   bot.add_cog(xkcd(bot))