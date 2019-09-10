<<<<<<< HEAD
import discord
import asyncio
import os
#---------------------#
import date_message
import jjambab_message
#---------------------#

client = discord.Client()
token = os.environ["BOT_TOKEN"]

@client.event
async def on_ready():
    print("현재 계정으로 로그인 합니다 : ")
    print(client.user.name)
    print(client.user.id)
    print("===================")
    await client.change_presence (game=discord.Game(name="봇 만들기", type=1))
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "!?" :
        await client.send_message (message.channel, "아아 테스트으으ㄴasf")     
    if message.content == "!오늘" :
        await client.send_message (message.channel, date_message.todays)   
    if message.content == "!내일" :
        await client.send_message (message.channel, date_message.tomorrows)  
    if message.content == "!어제" :
        await client.send_message (message.channel, date_message.yesterdays)
    if message.content == "!오늘 짬밥" :
        await client.send_message (message.channel, jjambab_message.today_result) 
        
client.run(token)
=======
1
>>>>>>> 3240305b8704446363d3272bf696d93f68ea1e2f
