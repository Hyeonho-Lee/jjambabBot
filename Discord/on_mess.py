import discord
import asyncio
#---------------------#
import date_message
import jjambab_message
#---------------------#

async def on_message(message):
    
    if message.author == client.user:
        return
    
    if message.content == "!?" :
        await client.send_message (message.channel, "아아 테스트으으ㄴasf")     
        
    #------------------------------------------------------------------------------#
        
    if message.content == "!오늘" :
        await client.send_message (message.channel, date_message.todays)
    if message.content == "!오늘 짬밥" :
        await client.send_message (message.channel, jjambab_message.today_result) 
        
    if message.content == "!내일" :
        await client.send_message (message.channel, date_message.tomorrows)  
    if message.content == "!내일 짬밥" :
        await client.send_message (message.channel, jjambab_message.tomorrow_result) 
        
    if message.content == "!어제" :
        await client.send_message (message.channel, date_message.yesterdays)
    if message.content == "!오늘 짬밥" :
        await client.send_message (message.channel, jjambab_message.yesterday_result) 
        
     #------------------------------------------------------------------------------#