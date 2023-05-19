import discord
from discord.ext import commands
import random
import aiohttp
import json
import time
import logging
#
# Crypto Cog
#

class crypto(commands.Cog, name="Crypto Commands"):
    """XkCD Commands"""

    def __init__(self, bot):
        self.bot = bot

    # BTC Prices
    @commands.slash_command(name='btc', description="BTC Price", brief="Get Current btc price")
    async def btc(self,ctx):
        async with ctx.typing():
            """Get Current btc price"""
            url = 'https://api.kraken.com/0/public/Ticker?pair=XBTUSD'
            async with aiohttp.ClientSession() as session:  # Async HTTP request
                raw_response = await session.get(url)
                response = await raw_response.text()
                response = json.loads(response)
                xbtusd = response['result']['XXBTZUSD']
                ask = "{:,.2f}".format(float(xbtusd['a'][0]))
                low = "{:,.2f}".format(float(xbtusd['l'][0]))
                high = "{:,.2f}".format(float(xbtusd['h'][0]))
                embed=discord.Embed(colour=discord.Colour.dark_gold())
                embed.set_author(name="BTC Price", icon_url="https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/btc.png")
                embed.add_field(name="Price", value=f"${ask}", inline=False)
                embed.add_field(name="Daily High", value=f"${high}", inline=True)
                embed.add_field(name="Daily Low", value=f"${low}", inline=True)
                embed.set_footer(text="prices from Kraken")
                await ctx.respond(embed=embed)
                message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
                logging.info(message_str)
                print(message_str)

    # Nano
    @commands.slash_command(name='nano',
                    description="nano price",
                    brief="Get Current nano price")
    async def nano(self,ctx):
        async with ctx.typing():
            """Get Current Nano price"""
            url = 'https://api.kraken.com/0/public/Ticker?pair=NANOUSD'
            async with aiohttp.ClientSession() as session:  # Async HTTP request
                raw_response = await session.get(url)
                response = await raw_response.text()
                response = json.loads(response)
                usd = response['result']['NANOUSD']
                ask = "{:,.2f}".format(float(usd['a'][0]))
                low = "{:,.2f}".format(float(usd['l'][0]))
                high = "{:,.2f}".format(float(usd['h'][0]))
                embed=discord.Embed(colour=discord.Colour.dark_blue())
                embed.set_author(name="Nano Price", icon_url="https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/nano.png")
                embed.add_field(name="Price", value=f"${ask}", inline=False)
                embed.add_field(name="Daily High", value=f"${high}", inline=True)
                embed.add_field(name="Daily Low", value=f"${low}", inline=True)
                embed.set_footer(text="prices from Kraken")
                await ctx.respond(embed=embed)
                message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
                logging.info(message_str)
                print(message_str)


    # Ethereum
    @commands.slash_command(name='eth',
                    description="ETH Price",
                    brief="Get Current Ethereum price")
    async def eth(self,ctx):
        async with ctx.typing():
            """Get Current Nano price"""
            url = 'https://api.kraken.com/0/public/Ticker?pair=ethusd'
            async with aiohttp.ClientSession() as session:  # Async HTTP request
                raw_response = await session.get(url)
                response = await raw_response.text()
                response = json.loads(response)
                usd = response['result']['XETHZUSD']
                ask = "{:,.2f}".format(float(usd['a'][0]))
                low = "{:,.2f}".format(float(usd['l'][0]))
                high = "{:,.2f}".format(float(usd['h'][0]))
                embed=discord.Embed(colour=discord.Colour.dark_blue())
                embed.set_author(name="Ethereum Price", icon_url="https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/eth.png")
                embed.add_field(name="Price", value=f"${ask}", inline=False)
                embed.add_field(name="Daily High", value=f"${high}", inline=True)
                embed.add_field(name="Daily Low", value=f"${low}", inline=True)
                embed.set_footer(text="prices from Kraken")
                await ctx.respond(embed=embed)
                message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
                logging.info(message_str)
                print(message_str)

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.


def setup(bot):
   bot.add_cog(crypto(bot))