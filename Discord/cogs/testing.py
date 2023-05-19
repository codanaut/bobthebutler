from unicodedata import name
import discord
from discord import client
from discord.embeds import Embed
from discord.ext import commands
import random
from discord.commands import SlashCommandGroup
import time
import logging

#
# Testing Cog
#




class testing(commands.Cog, name="Commands being tested"):
    """TestingCog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test',
                    description="test",
                    brief="testing brief.",
                    aliases=['test_me', 'testytest', 'testtesttest'],
                    pass_context=True)
    async def test(self,ctx):
        possible_responses = [
            'test',
            'testtesttest',
            'This is testing shit',
            'Oh yeah test that shit'
        ]
        message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
        logging.info(message_str)
        print(message_str)
        await ctx.send(random.choice(possible_responses))


    # Command Groups Test
    testgroup = SlashCommandGroup("testgroup","a test group")
    @testgroup.command(name = "hello", description = "Say hello to the bot")
    async def hello(self,ctx):
        message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
        logging.info(message_str)
        print(message_str)
        await ctx.respond("Hey!")
    

    # Get slash command ID
    @commands.slash_command(name='getid', description="gets id")
    async def getid(self,ctx):
        
        test = self.bot.get_application_command("btc", type=discord.commands.core.SlashCommand)
        print(test)
        
        message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
        logging.info(message_str)
        print(message_str)
        await ctx.respond(f"ID: {test.id} ")

    # Get slash command ID
    @commands.slash_command(name='getcommands', description="gets commands")
    async def getcommands(self,ctx):
        
        #test = [x.name for x in self.bot.commands]
        test = commands.Cog.get_commands(self)
        print(test)

        message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
        logging.info(message_str)
        print(message_str)
        await ctx.respond(f"ID: {test} ")

    
    # button class, uses MyView class under custom classes
    @commands.slash_command(name="button") # Create a slash command
    async def button(self,ctx):
        await ctx.respond("This is a button!", view=MyView()) # Send a message with our View class that contains the button

    


#
# Custom Classes
#


# Class views for buttons
class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
        @discord.ui.button(label="Click me!", style=discord.ButtonStyle.primary, emoji="😎") # Create a button with the label "😎 Click me!" with color Blurple
        async def button_callback(self, button, interaction):
            await interaction.response.send_message("You clicked the button!") # Send a message when the button is clicked



# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(testing(bot))
    

