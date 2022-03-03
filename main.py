import os
import discord
import funcoes

from discord.ext import commands
my_secret = os.environ['TOKEN']
bot = commands.Bot("!!")

@bot.event
async def on_ready():
    print('Fizemos login como {0.user}'.format(bot.user))

bot.run(os.getenv(my_secret))