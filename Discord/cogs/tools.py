import discord
from discord.ext import commands
import random
import aiohttp
import json
import time
import logging
#
# Tools Cog 
# 

class tools(commands.Cog, name="Random Tools Commands"):
    """TokeTimeCog"""

    def __init__(self, bot):
        self.bot = bot

    
    # List Servers
    @commands.slash_command(name='servers',
                    description="List Servers Bot is in",
                    brief="List Servers Bot is in",
                    aliases=['servers', 'serverlists'])
    async def servers(self,ctx):
        """List Server Bot is in."""
        servers = list(self.bot.guilds)
        newLine = '\n'
        
        await ctx.respond(f"**Connected on {str(len(servers))} servers:**{newLine}{newLine.join(server.name for server in servers)}")

        # Log
        message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
        logging.info(message_str)
        print(message_str)


    

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.

def setup(bot):
   bot.add_cog(tools(bot))