import colorsys
from email import message
from secrets import choice
from turtle import color, title
from typing import Optional
from datetime import datetime
from asyncio import events
from dis import disco
from http import client
from click import command
import discord
from discord.ext import commands
import asyncio
import random

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send('No')

    @commands.command()
    async def test2(self, ctx):
        if ctx.message.author.id == 482184210485084180:
            await ctx.send('https://cdn.discordapp.com/attachments/848489978454343684/990330844658954340/Screenshot_550.jpg')
        else:
            await ctx.send('Nehi. The real white dog has to do it.')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

    @commands.command()
    async def avatar(self, ctx, *,  avamember : discord.Member=None):
        if not avamember:
            avamember = ctx.message.author
        userAvatarUrl = avamember.avatar.url
        embed=discord.Embed(description=f'here is **{avamember}** avatar.', color=avamember.color)
        embed.set_author(name="IxxBot™", icon_url="https://cdn.discordapp.com/attachments/848489978454343684/985265069480874044/179db7cf8d2761a5f841d80faa8072e2_1.png")
        embed.set_image(url=userAvatarUrl)
        embed.set_footer(text=f'Requested by {ctx.message.author}')
        await ctx.send(embed=embed)

    @commands.command()
    async def ding(self, ctx):
        await ctx.send('Dong 🧏🏼')

    @commands.command()
    async def help(self, ctx):
        colors = (0xFFE577, 0xFEC051, 0xFF8866, 0xFF5D54, 0x392033)
        embed=discord.Embed(title="Commands", description="The commands used with IxxBot", color = random.choice(colors))
        embed.set_author(name="IxxBot", icon_url="https://cdn.discordapp.com/attachments/848489978454343684/985265069480874044/179db7cf8d2761a5f841d80faa8072e2_1.png")
        embed.add_field(name="!about", value="Shows the description of the bot.", inline=False)
        embed.add_field(name="!coolrate", value="The bot decides how cool you are.", inline=False)
        embed.add_field(name="!avatar (user)", value="Sends an enlarged profile picture of the mentioned user.", inline=False)
        embed.add_field(name="!members", value="Shows the number of members in the current server.", inline=False)
        embed.add_field(name="!ping", value="Shows the bot latency.", inline=False)
        embed.add_field(name="!userinfo (user)", value="Shows Information about the mentioned user.", inline=False)
        embed.add_field(name="!poll (question)", value="Generates a poll including the question.", inline=False)
        embed.add_field(name="!dm (user) (message)", value="Creates a DM and fowards the message to the mentioned user.", inline=False)
        embed.add_field(name="!clear (No. of messages) [ADMINS ONLY]", value="Deletes the number of messages inputted.", inline=False)
        embed.add_field(name="!sue (user)", value="Sues the mentioned user for a random price.", inline=False)
        embed.add_field(name="!move (user) (name of voice channel)", value="Moves the mentioned user into the mentioned voice channel.", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def members(self, ctx):
        guild = ctx.guild
        colors = (0x663FF1, 0xFBB443, 0xFF5353, 0xE0315B)
        embed=discord.Embed(title=f"Member count in {ctx.message.guild.name}", description=f"{guild.member_count} Members", color=random.choice(colors))
        embed.set_author(name="Member count")
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f"Member count requested by {ctx.message.author.name} | IxxBot™")
        await ctx.send(embed=embed)

    @commands.command(name= "userinfo", aliases=["ui", "mi"])
    async def userinfo(self, ctx, member : discord.Member=None):
        if not member:
            member = ctx.message.author
        memav = member.avatar_url
        embed=discord.Embed(title="User Informtation")
        embed.set_author(name="IxxBot", icon_url="https://cdn.discordapp.com/attachments/848489978454343684/985265069480874044/179db7cf8d2761a5f841d80faa8072e2_1.png")
        embed.set_thumbnail(url=memav)
        embed.add_field(name="Name", value=str(member), inline=False)
        embed.add_field(name="ID", value=member.id, inline=False)
        embed.add_field(name="Top Role", value=member.top_role.mention, inline=False)
        embed.add_field(name="Bot?", value=member.bot, inline=False)
        embed.add_field(name="Created on", value=member.created_at.strftime('%d/%m/%Y | %H:%M:%S'), inline=False)
        embed.add_field(name="Joined on", value=member.joined_at.strftime('%d/%m/%Y | %H:%M:%S'), inline=False)
        embed.add_field(name="Server booster", value=bool(member.premium_since), inline=False)
        embed.set_footer(text=f"Requested by {ctx.message.author.name} | IxxBot™")
        await ctx.send(embed=embed)

    @commands.command()
    async def testc(self, ctx):
        color = [0xEF325E, 0xC2135A, 0x620A94, 0x040A74, 0x0285D1]
        embed=discord.Embed(title="Test colors", description="Jareema", color=random.choice(color))
        await ctx.send(embed=embed)

    @commands.command()
    async def poll(self, ctx, *, content):
        colors = (0xEF325E, 0xC2135A, 0x620A94, 0x040A74, 0x0285D1)
        await ctx.message.delete()
        embed=discord.Embed(title=f"{ctx.author.name} asked a question!", description=content, color = random.choice(colors))
        embed.add_field(name='‎', value="🟢= **YES**, 🔴= **NO**", inline=True)
        embed.set_footer(text=f"Poll requested By {ctx.author} | IxxBot™")
        embed2 = await ctx.channel.send(embed=embed)
        await embed2.add_reaction('🟢')
        await embed2.add_reaction('🔴')

    @commands.command()
    async def rtest(self, message):
        new_msg = await message.channel.send("hello")
        await new_msg.add_reaction('🟢')

    @commands.command()
    @commands.is_owner()
    async def opdm(self, ctx, member : discord.Member, *, content):
        channel = await member.create_dm()
        await ctx.message.delete()
        await channel.send(content)

    @commands.command()
    async def dm(self, ctx, member : discord.Member , * , content):
        channel = await member.create_dm()
        await ctx.message.delete()
        await channel.send(f'**{ctx.message.author}** whispered: {content}')

    @commands.command()
    async def invite(self, ctx):
        server = ctx.guild
        link = commands.create_invite(destination=server, xkcd=True, max_age=0)
        await ctx.send(link)

    @commands.command()
    async def coolrate(self, ctx):
        colors = [0x132052, 0x4D2E5B, 0x7F2639, 0xC92716, 0xEC8005, 0xEDCEA8]
        if ctx.message.author == [604514843537440770]:
            embed = discord.Embed(title='Cool Rate', description= f"You will always be 100% cool. Owner moment frfr.", color=random.choice(colors))
            await ctx.send(embed = embed)
        else: 
            embed = discord.Embed(title='Cool Rate', description= f"You are {random.randrange(101)}% cool {ctx.author.mention}", color=random.choice(colors))
            await ctx.send(embed = embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, *, amount: int):
        await ctx.channel.purge(limit=amount+1)

    @commands.command()
    async def sue(self, ctx, avamember : discord.Member=None):
        randomnum = (random.randint(1, 10000000000))
        embed=discord.Embed(title=f"{ctx.message.author.name} Is suing {avamember}", description=f"**{ctx.message.author.name}** Is suing **{avamember}** for **${randomnum}**", color=0x000000)
        embed.set_author(name="SUE MOMENT")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/848489978454343684/985277687834763335/unknown.png")
        embed.add_field(name="Don't worry", value="Saul is there to help you 💸.", inline=True)
        embed.set_footer(text="IxxBot™ | 2022")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def spam(self, ctx, amount: int, *, message):
        for i in range(amount):
            await ctx.send(message)

    @commands.command()
    @commands.is_owner()
    async def testr(self, ctx, member : discord.Member=None):
        if not member:
            member = ctx.message.author
        role = discord.utils.get(self.bot.server.roles, name="WHITE DOGS")
        await self.bot.add_roles(member, role)

    @commands.command() # uses command decorators, in this case inside a cog
    @commands.is_owner()
    async def ban(self, ctx, user: discord.Member, *, reason): # The person banning someone has to ping the user to ban, and input a reason. Remove self if you are outside a cog.
        await ctx.guild.ban(user, reason=reason) # Bans the user.
        await user.send(f"You have been banned in {ctx.guild} for {reason}") # Private messages user.
        await ctx.send(f"{user} has been successfully banned.") # messages channel to tell everyone it worked

    @commands.Cog.listener()
    async def on_message(self, message, member : discord.Member=None):
        if message.content.lower() == "cook":
            randomnum = random.randint(1, 10000000000)
            embed=discord.Embed(title=f"{message.author.name}, WE NEED TO COOK", description="Walter White has asked you to cook.")
            embed.set_author(name="Did someone say cook?!")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/848489978454343684/986332243066777650/unknown.png")
            embed.add_field(name="COOKING WITH MR. WHITE", value=f"Walter White has asked you to make {randomnum} KG of Meth. [CLICK HERE](https://downloadmoreram.com) to make Meth!", inline=True)
            embed.set_footer(text="IxxBot™ | 2022")
            await message.channel.send(embed=embed)

        #if message.author.id in [482184210485084180]:
            #await message.add_reaction(':CARSEDDOG:965287363829985331')

        #if message.author.id in [412907322684473344]:
            #await message.add_reaction(':breachondregs:999414735936167956')

        if message.author.id in [293125663764774912]:
            await message.add_reaction(':wishaam:999415548515455076')

        if message.content.lower() == "hi":
            await message.channel.send("ހެލޯ")

        if message.content.lower() == "hello":
            await message.channel.send("ހެލޯ")
        
        #if message.author.id in [604514843537440770]:
        #   if message.channel.id == 990360398576381952:
        #      await message.add_reaction('a:verified:848642639138258984')
        #   else:
        #      return

        #a:verified:848642639138258984 = verified logo#

    @commands.command()
    async def about(self, ctx):
        embed=discord.Embed(title="About me ", description="A bot with a little bit of everything.", color=0x000000)
        embed.set_author(name="IxxBot", icon_url="https://cdn.discordapp.com/attachments/848489978454343684/985265069480874044/179db7cf8d2761a5f841d80faa8072e2_1.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/848489978454343684/985265069480874044/179db7cf8d2761a5f841d80faa8072e2_1.png")
        embed.add_field(name="Owner", value="@Ixxlhey#7587 <a:crown_gif:848767868967714826>", inline=True)
        embed.add_field(name="No. of Servers", value=f"IxxBot is currently in {len(self.bot.guilds)} servers!", inline=False)
        embed.add_field(name="Status", value=f"Under Maintenance <:yi:848649134235189298>", inline=False)
        embed.set_footer(text="IxxBot™ | 2022")
        await ctx.send(embed=embed)

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def move(self, ctx, member : discord.Member, channel : discord.VoiceChannel):
        await member.move_to(channel)
        await ctx.reply(f"Moved **{member}** to **{channel}**")

def setup(bot):
    bot.add_cog(test(bot))