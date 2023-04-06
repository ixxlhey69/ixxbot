import discord
from discord.ext import bridge
import asyncio
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(debug_guilds=[848489978454343681])

#################################################################################################################################################################################

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

async def ch_pr():
    await bot.wait_until_ready()
    
    statuses = ["Jareema", "!about", "Owner | @ixxlhey#7587", "White dog association", f"Currently in {len(bot.guilds)} servers!", "Under maintenance"]

    while not bot.is_closed():

        status = random.choice(statuses)

        await bot.change_presence(activity=discord.Game(name=status))
        
        await asyncio.sleep(5)

bot.loop.create_task(ch_pr())

#################################################################################################################################################################################

#Commands#
#################################################################################################################################################################################

@bot.command(description="Sends bot's latency")
async def ping(ctx):
    await ctx.respond(f"Pong! The bot's latency is **{bot.latency}**")

@bot.command()
async def add(ctx, first: discord.Option(int), second: discord.Option(int)):
  sum = first + second
  await ctx.respond(f"The sum of {first} and {second} is {sum}.")

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension("cogs." + file[:-3])

print('cog loaded')
