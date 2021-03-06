import discord
import os
import dotenv
from discord.ext import commands
from discord_slash import SlashCommand

from cogs.statut import test
from cogs.tictac import tic

# Recupere le token dans le fichier .env
dotenv.load_dotenv()
token = os.getenv('TOKEN')

# Prefix du bot
bot = commands.Bot(command_prefix = "/", description = "EK Bot")
slash = SlashCommand(bot, sync_commands = True)

# Commandes
bot.add_cog(test(bot))
bot.add_cog(tic(bot))

bot.run(token)
