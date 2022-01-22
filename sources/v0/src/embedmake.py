import discord

def helpEmbed():
    rEmbed = discord.Embed(
        title="Help",
        description="WallAlley.bot help page",
        colour=discord.Colour.from_rgb(123, 7, 213)
    )
    rEmbed.add_field(name="h", value="h", inline=False)
          
    rEmbed.set_footer(text="© MOSEMBIK")

    return rEmbed

def priceEmbed(data):
    if data['response'] == 'ERROR' :
        rEmbed = discord.Embed(
            title="{ERROR} price",
            description="Last price for {ERROR}.",
            colour=discord.Colour.from_rgb(123, 7, 213)
        )
        rEmbed.add_field(name="CODE 404", value="Asset not found.", inline=False)
        rEmbed.set_footer(text="© MOSEMBIK")
        return rEmbed

    rEmbed = discord.Embed(
        title="Price",
        description="Last price for {}.",
        colour=discord.Colour.from_rgb(123, 7, 213)
    )
    rEmbed.add_field(name="p", value="p", inline=False)
          
    rEmbed.set_footer(text="© MOSEMBIK")

    return rEmbed

def trackEmbed(data):
    if data['response'] == 'ERROR' :
        rEmbed = discord.Embed(
            title="{ERROR} price",
            description="Last price for {ERROR}.",
            colour=discord.Colour.from_rgb(123, 7, 213)
        )
        rEmbed.add_field(name="CODE 404", value="Asset not found.", inline=False)
        rEmbed.set_footer(text="© MOSEMBIK")
        return rEmbed
        
    rEmbed = discord.Embed(
        title="Track",
        description="Track {} statistics.",
        colour=discord.Colour.from_rgb(123, 7, 213)
    )
    rEmbed.add_field(name="t", value="t", inline=False)
          
    rEmbed.set_footer(text="© MOSEMBIK")

    return rEmbed