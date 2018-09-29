import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


Client = discord.Client()
client = commands.Bot(command_prefix="?")

@client.event
async def on_message(message):
    if message.content.upper().startswith('?SALES'):
        userID = message.author.id
        server = client.get_server("490938256683302912")
        args = message.content.split(" ")
        embed=discord.Embed(title=":shopping_cart: Item requested", description="Someone requested an item!", color=0x00ff00)
        embed.add_field(name="Game", value="%s" % (args[1]), inline=False)
        embed.add_field(name="Item", value="%s" % (args[2]), inline=False)
        embed.add_field(name="Quantity", value="%s" % (args[3]), inline=False)
        embed.add_field(name="User", value="<@%s> requested" % (userID), inline=False)
        await client.send_message(server.get_channel("490942613269250048"), embed=embed)
        await client.send_message(message.channel, "Thank you for the purchase!")
    if message.content.upper().startswith('?ANNOUNCE'):
        if "490942293944041484" in [role.id for role in message.author.roles]:
            server = client.get_server("490938256683302912")
            args = message.content.split(" ")
            await client.send_message(server.get_channel("491676268853723138"), "@everyone %s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You are not an admin")
    if message.content.upper().startswith('?WARNING'):
        if message.author.id == "268087923751124992":
            server = client.get_server("490938256683302912")
            args = message.content.split(" ")
            embed=discord.Embed(title=":warning: Warning from Admin", description="Warning from an adminstator.", color=0x00ff00)
            embed.add_field(name="Warning Reason", value="%s @here" % (args[1]), inline=False)
            await client.send_message(server.get_channel("490942613269250048"), embed=embed)
        else:
            await client.send_message(message.channel, "You do not meet the requirements to complete this action.") 

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Handling sales! Sales will be accepted faster!"))



client.run("NDkxMjc5MTAyMDgzMzM0MTQ1.DoLciw.oIOSzGMGWz9jZDQQ2tQDCLlN3Mg")
