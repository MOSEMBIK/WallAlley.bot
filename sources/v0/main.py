from config import token

import json
import time
import asyncio

import discord
from discord.ext import commands
from discord.ext import tasks
from discord_slash import SlashCommand

TOKEN = token
bot = commands.Bot("w!")
bot.remove_command('help')
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print("WallAlley.bot has join.")