import discord
from discord.ext import commands
import time
import logging

#
# example Cog 
#
# Make sure to change class name in line 13 & 36
# 

class help(commands.Cog):
    

    def __init__(self, bot):
        self.bot = bot

    
    # List Servers
    @commands.slash_command(name='help', description="Help & About")
    async def help(self,ctx):
        embed=discord.Embed(title="Help & About", description="", color=discord.Colour.dark_blue())
        embed.add_field(name="**Command Help**", value="----------\nAccess all commands using /command-name. Typing / alone displays available options.", inline=False)
        embed.add_field(name="**ChatBot**", value="----------\n***BobTheButler*** functions seamlessly as a command-free chatbot through Gemini or ChatGPT integration. Simply mention <@714703250649120778> in channels, or direct message for private interactions.", inline=False)
        embed.add_field(name="**About**", value="----------\nThis is a personal side project, if you need support or want a feature added then contact <@301100786199560194> or vist the support server: https://discord.gg/CvKeEPm49p", inline=False)
        embed.add_field(name="**GitHub**", value="----------\nStay informed and explore new features by visiting our GitHub: https://github.com/codanaut/bobthebutler. \nFor suggestions or to report an issue, please use the GitHub issues section.", inline=False)
        await ctx.respond(embed=embed)

        message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
        logging.info(message_str)
        print(message_str)

    

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.

def setup(bot):
   bot.add_cog(help(bot))