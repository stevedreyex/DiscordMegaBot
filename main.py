#導入 Discord.py
import discord
#client 是我們與 Discord 連結的橋樑
client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} is online!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("!hello") or message.content.startswith("/hello"):
        await message.channel.send("Hello MDFK ><")


with open('./token.log') as f:
    contents = f.read()

client.run(contents) #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面