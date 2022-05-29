import discord
from discord.ext import commands
from discord_slash import cog_ext


class tic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Tic tac... BOOOOOM")
    async def tic(self, ctx):
            await ctx.send("tac !")

    @cog_ext.cog_slash(name="tic", description="Tic tac... BOOOOOM")
    async def tic(self, ctx):
            await ctx.send("tac !")
            print("Test")
