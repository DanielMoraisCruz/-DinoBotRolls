import os, discord
from discord.ext import commands


bot = commands.Bot("!!")

@bot.event
async def on_ready():
    print('Fizemos login como {0}'.format(bot.user))

@bot.command(name = "oi")
async def mandar_oi(ctx):
    name = ctx.author.name

    resposta = "ola, " + name

    await ctx.send(resposta)






bot.run(os.environ['TOKEN'])