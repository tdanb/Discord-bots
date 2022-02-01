#client id: 937989149988892673
# token: [omitted]
#52288

#https://discord.com/oauth2/authorize?client_id=937989149988892673&scope=bot&permissions=52288

# required imports
import discord
import time
import asyncio

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

    # standard pleasant responses
    if "!hi" in message.content.lower():
        await message.channel.send("Hello 😁")
    elif "see you again" in message.content.lower():
        await message.channel.send("I'm looking forward to talking to you! 🤗")
    elif "!intro" in message.content.lower():
        await message.channel.send("Ready to learn about the state of covid in ON, Canada?!")
    if "thank you" in message.content.lower():
            await message.channel.send("No problem! 😉")

    # link to the current number of covid cases
    elif "!cases" in message.content.lower():
        await message.channel.send("https://www.covid19inontario.com/")

    # covid related news reports
    elif "!news" in message.content.lower():
        await message.channel.send("https://www.bing.com/news/search?q=COVID+Cases+In+Ontario+Today&qpvt=covid+cases+in+ontario+today&FORM=EWRE")

    # covid hospitalization
    elif "!hospitalization" in message.content.lower():
        await message.channel.send("https://covid-19.ontario.ca/data/hospitalizations")

    # link to the vaccine update
    elif "!vaccine" in message.content.lower():
        await message.channel.send("https://covid-19.ontario.ca/data")

    # link to the current number of covid cases
    elif "!symptom" in message.content.lower():
        await message.channel.send("https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection/symptoms.html")


    # logout
    elif "!logout" == message.content.lower():
        await client.close()

client.run("[token omitted]")