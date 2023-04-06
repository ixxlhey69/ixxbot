import discord
from discord.ext import commands
import random
from discord.ext import tasks
import asyncio
import os

bot = commands.Bot(command_prefix='-')

bot.remove_command('help')

@bot.event
async def on_ready():
    for filename in os.listdir('./cogs'):
        if filename == '__pycache__':
            return
        else:
            bot.load_extension(f'cogs.{filename[:-3]}')
            print('Loaded: ',filename)
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send(f'Hey there! Thank you for inviting me into **{guild}** server :D !')
        break

async def ch_pr():
    await bot.wait_until_ready()
    
    statuses = ["Jareema", "-about", "Owner | @ixxlhey#7587", "White dog association", f"Currently in {len(bot.guilds)} servers!", "Under maintenance"]

    while not bot.is_closed():

        status = random.choice(statuses)

        await bot.change_presence(activity=discord.Game(name=status))
        
        await asyncio.sleep(5)

bot.loop.create_task(ch_pr())


bot.load_extension("jishaku")
