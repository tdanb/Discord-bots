#client id: 937985946698264596
#token: [omitted]
# 67176512

#https://discord.com/oauth2/authorize?client_id=937985946698264596&scope=bot&permissions=67176512

# required imports
import discord
import time
import asyncio
from discord.ext import commands
#imports to create member report
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

client = discord.Client()

@client.event 
# establishing user at login
async def on_ready():
    print(f"{client.user} has logged on")

@client.event 
# establishing reactions to certain messages
async def on_message(message):
    guild = client.get_guild(937958472903983124)

    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    # printing member count
    if "!member count" in message.content.lower():
        await message.channel.send(f"```py\n{guild.member_count}```")

    # standard pleasant responses
    elif "!hi" in message.content.lower():
        await message.channel.send("Howdy :)")
    elif "see you again" in message.content.lower():
        await message.channel.send("I'm so glad you're back!")
    elif "!intro" in message.content.lower():
        await message.channel.send("I'm your average discord bot 😉 and welcome to the server!")
    elif "thank" in message.content.lower():
        await message.channel.send("No problem! 😁")

    # logout
    elif "!logout" == message.content.lower():
        await client.close()

    # motivational picture 
    elif "hard" in message.content.lower():
        file = discord.File("average-bot/images/catMotivation.png", filename="average-bot/images/catMotivation.png")
        await message.channel.send("Here is a motivational cat poster to help 🙂", file=file)

    # displaying a cat photo
    elif "cat" in message.content.lower():
        file = discord.File("average-bot/images/cat.jpg", filename="average-bot/images/cat.jpg")
        await message.channel.send("🐱", file=file)

    # display a gif
    elif "animal" in message.content.lower():
        file = discord.File("average-bot/images/cute.gif", filename="average-bot/images/cute.gif")
        await message.channel.send("", file=file)

client.run("OTM3OTg1OTQ2Njk4MjY0NTk2.YfjtfA.smBGZhBeCuFmq16ypwfSnx8eQxA")
