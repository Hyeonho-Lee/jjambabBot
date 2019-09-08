import discord
import asyncio

client = discord.Client()
token = "NjIwMTM3NTY0ODQxNTc0NDIx.XXSa_g.86uJbhZaahja2XuduHHFNW-HM_E"

@client.event
async def on_ready():
    print("현재 계정으로 로그인 합니다 : ")
    print(client.user.name)
    print(client.user.id)
    print("===================")
    await client.change_presence (game=discord.Game(name="봇 만들어 보는중", type=1))
    

@client.event
async def on_message():
    if message.author == client.user:
        return
    if message.content == "!" :
        await client.send_message (message.channel, "아아 테스트으으")
    if message.content == "!아아" :
        await client.send_message (message.channel, "예에에")        
        
client.run(token)