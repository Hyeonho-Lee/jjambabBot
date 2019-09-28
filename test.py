import discord
import asyncio
import os
import re
import sys
#---------------------#
import date_message
import jjambab_message
import work_message
#---------------------#

client = discord.Client()

def set_embed(titles, descriptions):
    embeds = discord.Embed(title = titles, description = descriptions, color=0xff7b5c)
    embeds.set_footer(text = date_message.todayT)
    return embeds

##########################################################################

@client.event
async def on_ready():
    print("===================")
    print("현재 계정으로 로그인 합니다 : ")
    print(client.user.name)
    print(client.user.id)
    print("===================")
    game = discord.Game("RPC봇 테스트")
    await client.change_presence(status=discord.Status.online, activity=game)

#########################################################################
    
@client.event
async def on_message(message):    
    
    if message.author == client.user:
        return
    
    if message.content.startswith("/?"):
        await message.channel.send(embed=set_embed("단결! 명령어를 불러드렸습니다!!", "/(오늘, 내일, 어제) 짬밥\n/(원하는 일자)일 짬밥\n/px"))
        
    search_day = ""
    
    last_text = message.content
    result_day = re.findall("\d+", last_text)
    for result in result_day:
        search_day = result
        
    if message.content == "/%s일 짬밥"%search_day:
        title, description = jjambab_message.search_jjambab(search_day)
        await message.channel.send(embed=set_embed(title, description))
    
    if message.content.startswith("/오늘 짬밥"):
        title, description = jjambab_message.result_jjambab("오늘")
        await message.channel.send(embed=set_embed(title, description))
        
    if message.content.startswith("/내일 짬밥"):
        title, description = jjambab_message.result_jjambab("내일")
        await message.channel.send(embed=set_embed(title, description))
        
    if message.content.startswith("/어제 짬밥"):
        title, description = jjambab_message.result_jjambab("어제")
        await message.channel.send(embed=set_embed(title, description))
        
    if message.content.startswith("/px"):
        title = "단결! px이용시간 입니다!!"
        description = "==========평일==========\n10:30 ~ 11:50\n13:00 ~ 17:00 \n 18:00 ~ 19:30\n==========휴일==========\n14:00 ~ 17:30\n========================"
        await message.channel.send(embed=set_embed(title, description))
    
    index = ""
    date = ""
    writer = ""
    time = ""
    content = ""
    
    if message.content == "/근무":
        title, description = work_message.result_work("근무")
        await message.channel.send(embed=set_embed(title, description))
    
    last_text = message.content
    result_text = re.findall("\w+", last_text)
    #print(result_text)
    result_len = len(result_text)

    if message.content.startswith("/근무 추가"):
        if result_len == 6:
            date = result_text[2]
            writer = result_text[3]
            time = result_text[4]
            content = result_text[5]
        else:
            return
        
    if message.content == "/근무 추가 %s,%s,%s,%s"%(date,writer,time,content):
        last_index = work_message.last_index()
        work_message.work_write(last_index,date,writer,time,content,last_index+1)
        title, description = work_message.result_work("근무 추가")
        await message.channel.send(embed=set_embed(title, description))
        
    test = ""
    
    if message.content == "/근무 보기":
        last_index = work_message.last_index()
        index,date,writer,time,content = work_message.work_all_load()
        title, description = work_message.result_work("근무 보기")
        test = "번호 | 날짜 | 작성자 | 시간 | 내용"
        test += "\n---------------------------------------------"
        for i in range(0,last_index-1):
            text = "\n" + index[i] + " | " + date[i] + " | " + writer[i] + " | " + time[i] + " | " + content[i]
            test += text
            test += "\n---------------------------------------------"
        test += "\n"
        #print(test)
        await message.channel.send(embed=set_embed(title, test))
    
    if message.content == "/근무 삭제":
        last_index = work_message.last_index()
        if last_index <= 2:
            title, description = work_message.result_work("근무 삭제 실패")
            await message.channel.send(embed=set_embed(title, test))
        else:
            work_message.work_delete(last_index)
            title, description = work_message.result_work("근무 삭제")
            await message.channel.send(embed=set_embed(title, test))
        
    #delete_index = ""
    
    #last_text = message.content
    #result_text = re.findall("\d+", last_text)
    #for result in result_text:
        #delete_index = result
        
    #if message.content == "/근무 삭제 %s"%delete_index:
        #last_index = work_message.last_index()
        #work_message.work_delete(last_index)
        #title, description = work_message.result_work("근무 삭제")
        #await message.channel.send(embed=set_embed(title, test))

#########################################################################

client.run("NjIwMTM3NTY0ODQxNTc0NDIx.XY7g2w.cKYz7nlHSwXlYu_81aBZVlFcsnk")
