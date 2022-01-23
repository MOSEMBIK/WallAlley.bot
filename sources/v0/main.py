from src.config import token
from src.embedmake import *
from src.function import *

import json
import time
import asyncio

import yfinance as yf

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
    await ctx.send("Let me find the asset...")
    data = await get_Price(message.upper())
    embed = priceEmbed(data)
    await ctx.send(embed=embed)
@slash.slash(name="Price", description="Return last price for the asked asset.")
async def _price(ctx, message):
    await price(ctx, message)

# Track
@bot.command()
async def track(ctx, message):
    await ctx.send("Let me find the asset...")
    data = await get_Stats(message.upper())
    embed = trackEmbed(data)
    await ctx.send(embed=embed)
@slash.slash(name="Track", description="Return stats for the asked asset.")
async def _track(ctx, message):
    await track(ctx, message)


bot.run(TOKEN)