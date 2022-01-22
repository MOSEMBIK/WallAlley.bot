import discord

def helpEmbed():
    notifEmbed = discord.Embed(
        title="Help",
        description="WallAlley.bot help page",
        colour=discord.Colour.from_rgb(123, 7, 213)
    )
    notifEmbed.add_field(name="h", value="h", inline=False)
          
    notifEmbed.set_footer(text="© MOSEMBIK")

    return notifEmbed

def priceEmbed():
    notifEmbed = discord.Embed(
        title="Price",
        description="Last price for {}.",
        colour=discord.Colour.from_rgb(123, 7, 213)
    )
    notifEmbed.add_field(name="p", value="p", inline=False)
          
    notifEmbed.set_footer(text="© MOSEMBIK")

    return notifEmbed

def trackEmbed():
    notifEmbed = discord.Embed(
        title="Track",
        description="Track {} statistics.",
        colour=discord.Colour.from_rgb(123, 7, 213)
    )
    notifEmbed.add_field(name="t", value="t", inline=False)
          
    notifEmbed.set_footer(text="© MOSEMBIK")

    return notifEmbed