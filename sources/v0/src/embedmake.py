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
        title=f"{data['name']}",
        description=f"Last price for {data['symbol']}.",
        colour=discord.Colour.from_rgb(123, 7, 213)
    )
    rEmbed.add_field(name="Last price", value=f"{data['price']}", inline=False)
    rEmbed.add_field(name="Daily change", value=f"{data['dchange']}", inline=False)
          
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
        title=f"{data['name']}",
        description=f"Tracked {data['symbol']} statistics. \n _{data['sector']}_",
        colour=discord.Colour.from_rgb(123, 7, 213)
    )
    rEmbed.add_field(name="Last price", value=f"{data['price']}", inline=False)
    rEmbed.add_field(name="Daily change", value=f"{data['dchange']}", inline=False)
    
    rEmbed.add_field(name="Day high", value=f"{data['dhigh']}", inline=True)
    rEmbed.add_field(name="|", value="**|**", inline=True)
    rEmbed.add_field(name="Day low", value=f"{data['dlow']}", inline=True)
          
    rEmbed.set_footer(text="© MOSEMBIK")

    return rEmbed