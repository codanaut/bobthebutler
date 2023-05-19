import discord
from discord.ext import commands
import random
import time
import logging

#
# Toke Time Cog
#

class TokeTime(commands.Cog, name="Toke Time Commands"):
    """TokeTimeCog"""

    def __init__(self, bot):
        self.bot = bot

    # Toke/Burn/Smoke saying
    @commands.slash_command(name='toke',
                    description="Its time to toke",
                    brief="Its Time To Burn!",
                    aliases=['toke', 'lightup', 'smoke'])
    async def burn(self,ctx):
        """This is for testing random things."""
        user = ctx.author
        icon = "<:leaf:714677760689438750>"
        #icon = "<:rastalion:784896784764895273>"
        content = '{0} wants to burn! {1}'.format(user.mention,icon)

        qList = ['{} wants to burn!"','{} is lighting up!!!',
                '{1}Toke{1}Toke{1}Toke{1}',
                'Puff, Puff, Pass',
                'its all gone up in smoke',
                'everyone take a hit',
                'hit that shit yo',
                '{1}',
                '<:rastaleaf:714186541282623509>',
                '<a:weedbag:784878760650342401>',
                '<a:bong:725837929200484474>'
                ]
        ranSaying = random.choice(qList)
        msg = ranSaying.format(user.mention,icon)
        await ctx.respond(msg)
        # Log
        message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
        logging.info(message_str)
        print(message_str)
    

    # Random Gif
    @commands.slash_command(name='gif',
                    description="random gif",
                    brief="random gif.",
                    aliases=['gif_me', 'gifgif', 'gifgifgif'],
                    pass_context=True)
    async def random_gif(self,ctx):
        possible_responses = [
            'https://tenor.com/view/smoke-cigarettes-khalifa-gif-14617129',
            'https://tenor.com/view/someweed-red-eyes-somebush-tgif-gif-15372603',
            'https://media.giphy.com/media/2Y8Iq3xe121Ba3hUAM/giphy.gif',
            'https://media.giphy.com/media/nxMiyZea0AQY8/giphy.gif',
            'https://media.giphy.com/media/aMfbIklQXV29y/giphy.gif',
            'https://media.giphy.com/media/yogEmgIWxh72w/giphy.gif',
            'https://media.giphy.com/media/CoB1VA7w5cAjC/giphy.gif',
            'https://media.giphy.com/media/RSEuJxiw2H24U/giphy.gif',
            'https://media.giphy.com/media/xT9DPn3MABvIwlubgk/giphy.gif'
        ]
        await ctx.respond(random.choice(possible_responses))

        # Log
        message_str = f"{time.strftime('%m/%d/%y %I:%M%p')} - User:{ctx.author} - Server:{ctx.guild} - Command: /{ctx.command} "
        logging.info(message_str)
        print(message_str)


# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.


def setup(bot):
   bot.add_cog(TokeTime(bot))