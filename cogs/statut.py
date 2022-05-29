import discord
from discord.ext import commands

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity = discord.Streaming(name = "une partie de sudoku...", url = "https://www.twitch.tv/eyko_"))
        print(f"{self.bot.user.name} est connecté au serveur !")
        print(f"-------------------------------")