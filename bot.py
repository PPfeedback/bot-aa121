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

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Handling sales!"))



client.run("NDkwOTQyNTAxOTQ4MjI3NTk3.DoGPOw.waPWEoRlm_O9996ggJOfDT4niOM")
