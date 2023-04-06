import discord
from discord.ext import commands
from discord.commands import slash_command, Option

class avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Sends avatar of the mentioned user.")
    async def avatar(self, ctx, username : discord.Member=None):
        if not username:
            username = ctx.author
        userAvatarUrl = username.avatar.url
        embed=discord.Embed(description=f'here is **{username}** avatar.', color=username.color)
        embed.set_author(name="IxxBot™", icon_url="https://cdn.discordapp.com/attachments/848489978454343684/985265069480874044/179db7cf8d2761a5f841d80faa8072e2_1.png")
        embed.set_image(url=userAvatarUrl)
        embed.set_footer(text=f'Requested by {ctx.author}')
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(avatar(bot))