import discord
from discord.ext import commands
from discord.commands import slash_command, Option

class View(discord.ui.View):
    @discord.ui.button(label="D3aDz", style=discord.ButtonStyle.primary, emoji="💀")
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked the button!", ephemeral=True)

class Buttons(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="The button command")
    async def button(self, ctx):
        await ctx.respond("Become the dead", view=View())

def setup(bot):
    bot.add_cog(Buttons(bot))