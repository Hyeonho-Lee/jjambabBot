import discord
import asyncio
import os
#---------------------#
import date_message
import jjambab_message
import on_mess
#---------------------#

client = discord.Client()

########################################################################################

@client.event
async def on_ready():
    print("현재 계정으로 로그인 합니다 : ")
    print(client.user.name)
    print(client.user.id)
    print("===================")
    await client.change_presence (game=discord.Game(name="봇 만들기", type=1))
    
########################################################################################


@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    if message.content == "!?" :
        await client.send_message (message.channel, "아아 테스트으으ㄴasf")     
        
    #------------------------------------------------------------------------------#

    if message.content == "/오늘" :
        #await client.send_message (message.channel, date_message.todays)
        embed = discord.Embed(title = "날짜", description=date_message.todays, color=0xff7b5c)
        embed.set_footer(text=date_message.todayT)
        await client.send_message(message.channel, embed=embed)
        
    if message.content == "/오늘 짬밥" :
        #await client.send_message (message.channel, jjambab_message.today_result) 
        embed = discord.Embed(title = jjambab_message.today_result, description = jjambab_message.todays_result, color=0xff7b5c)
        embed.set_footer(text=date_message.todayT)
        await client.send_message(message.channel, embed=embed)
    
    if message.content == "/내일" :
        await client.send_message (message.channel, date_message.tomorrows)  
        
    if message.content == "/내일 짬밥" :
        #await client.send_message (message.channel, jjambab_message.tomorrow_result) 
        embed = discord.Embed(title = jjambab_message.tomorrow_result, description = jjambab_message.tomorrows_result, color=0xff7b5c)
        embed.set_footer(text=date_message.todayT)
        await client.send_message(message.channel, embed=embed)
        
    if message.content == "/어제" :
        await client.send_message (message.channel, date_message.yesterdays)
        
    if message.content == "/어제 짬밥" :
        #await client.send_message (message.channel, jjambab_message.yesterday_result) 
        embed = discord.Embed(title = jjambab_message.yesterday_result, description = jjambab_message.yesterdays_result, color=0xff7b5c)
        embed.set_footer(text=date_message.todayT)
        await client.send_message(message.channel, embed=embed)


token = 'NjIwMTM3NTY0ODQxNTc0NDIx.XXtssg.CodzrJKDYyCt-_OD88Ng2tdjEM0'
client.run(token)

"""
import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("24시간 실험중")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!테스트"):
        await message.channel.send("안녕하세요")


client.run("NjIwMTM3NTY0ODQxNTc0NDIx.XXtssg.CodzrJKDYyCt-_OD88Ng2tdjEM0")
버전이 봐꼇슴 그래서 저걸로 바꾸자
"""
