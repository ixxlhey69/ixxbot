import discord
from discord.ext import commands
from discord.commands import slash_command, Option

class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Title"))
        self.add_item(discord.ui.InputText(label="Confession", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Modal Results")
        embed.add_field(name="Title of confession.", value=self.children[0].value)
        embed.add_field(name="Confession.", value=self.children[1].value, inline=False)
        channel = discord.Bot.get_channel(990351568371089478)
        await channel.send(embeds=[embed])

class modal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def modal_slash(self, ctx: discord.ApplicationContext):
        """Shows an example of a modal dialog being invoked from a slash command."""
        modal = MyModal(title="Confession")
        await ctx.send_modal(modal)

def setup(bot):
    bot.add_cog(modal(bot))