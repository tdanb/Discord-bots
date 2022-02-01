#client id: 937985946698264596
#token: OTM3OTg1OTQ2Njk4MjY0NTk2.YfjtfA.jUbW_-RxG1B95svbEeFNK6Pkjcg
# 67176512

#https://discord.com/oauth2/authorize?client_id=937985946698264596&scope=bot&permissions=67176512

# required imports
import discord
import time
import asyncio
#imports to create member report
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

client = discord.Client()

# gathering data from the server on online, offline and idle members
def member_report (guild):
    online = 0
    offline = 0
    idle = 0

    for i in guild:
        if str(i.status) == "online":
            online += 1
        elif str(i.status) == "offline":
            offline += 1
        else:
            idle += 1
    return online, offline, idle

# continously gathering data from the status of server members in the background
async def member_report_background():
    await client.wait_until_ready()
    guild = client.get_guild(937958472903983124)

    # loop to gather member status
    while not client.is_closed():
        try:
            online, offline, idle = member_report(guild)
            with open("memberReport.csv","a") as f:
                f.write(f"{int(time.time())},{online},{offline},{idle}\n")

                df = pd.read_csv("memberReport.csv",names=['time','online','offline','idle'])
                df['date'] = pd.to_datetime(df['time'],unit='s')
                df['total']=df['online']+df['offline']+df['idle']
                df.drop("time",1,inplace=True)
                df.set_index("date",inplace=True)

                df.plot()
                plt.clf()
                plt.legend()
                plt.savefig("status.png")
            # interval member status is recorded
            await asyncio.sleep(5)

        except Exception() as e:
            print(str(e))
            await asyncio.sleep(5)


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
        await message.channel.send("I'm your average discord bot 😉")

    # create member report 
    elif "!status report" in message.content.lower():
        online, offline, idle = member_report(guild)

        await message.channel.send(f"```py\nOnline:{online}.\nIdle/busy/dnd:{idle}.\nOffline:{offline}```")
        file = discord.File("status.png",filename="status.png")
        await message.channel.send("status.png", file=file)

    # logout
    elif "!logout" == message.content.lower():
        await client.close()

client.loop.create_task(member_report_background())
client.run("OTM3OTg1OTQ2Njk4MjY0NTk2.YfjtfA.jUbW_-RxG1B95svbEeFNK6Pkjcg")