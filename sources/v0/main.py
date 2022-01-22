from config import token
from embedmake import *

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

# ------------------------------------------------

# ------------------------------------------------
# Command

# Help
@bot.command()
async def help(ctx):
    embed = helpEmbed()
    await ctx.send(embed=embed)
@slash.slash(name="Help", description="Return the WallAlley.bot help page.")
async def _help(ctx):
    await help(ctx)

# Price
@bot.command()
async def price(ctx, message):
    embed = priceEmbed()
    await ctx.send(embed=embed)
@slash.slash(name="Price", description="Return last price for the asked asset.")
async def _price(ctx, message):
    await price(ctx, message)

# Order
@bot.command()
async def track(ctx, message):
    embed = trackEmbed()
    await ctx.send(embed=embed)
@slash.slash(name="Track", description="Return stats for the asked asset.")
async def _track(ctx):
    await track(ctx)


bot.run(TOKEN)