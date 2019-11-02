import discord
import asyncio
import os
import re
import sys
#---------------------#
import date_message
import jjambab_message
import work_message
import calculator_message
import scheduler_message
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
    game = discord.Game("R.PC Bot Online")
    await client.change_presence(status=discord.Status.online, activity=game)
    scheduler_message.sched_start()
    channel = client.get_channel(622749469313728553)
	#364719246820769792 배그서버
	#622749469313728553 5생실험실
    is_true = 0
    while True:
        try:
            if int(date_message.todayTimeH) == 6 and int(date_message.todayTimeM) == 30 and int(date_message.todayTimeS) == 5 and is_true == 0:
                is_true = 1
                last_index = calculator_message.last_index()
                name,date_0,date_1,result_date,percent = calculator_message.calculator_all_load()
                title, description = calculator_message.result_calculator("전역 보기")
                test = "이름 | 전역일 | 입대일 | 일자 | 퍼센트"
                test += "\n-----------------------------------------------------------"
                for i in range(0,last_index-1):
                    text = "\n" + name[i] + " | " + date_1[i] + " | " + date_0[i] + " | " + result_date[i] + " | " + percent[i]
                    test += text
                    test += "\n-----------------------------------------------------------"
                test += "\n"
                #print(test)
                await channel.send(embed=set_embed(title, test))
                is_true = 0
            if int(date_message.todayTimeH) == 7 and int(date_message.todayTimeM) == 0 and int(date_message.todayTimeS) == 5 and is_true == 0:
                is_true = 1
                jjambab_message.reload_jjambab()
                title, description = jjambab_message.result_jjambab("아침")
                await channel.send(embed=set_embed(title, description))
                is_true = 0
            if int(date_message.todayTimeH) == 12 and int(date_message.todayTimeM) == 0 and int(date_message.todayTimeS) == 5 and is_true == 0:
                is_true = 1
                await channel.send(embed=set_embed("밥시간 알림", "점심 30분전 입니다"))
                is_true = 0
            if int(date_message.todayTimeH) == 12 and int(date_message.todayTimeM) == 30 and int(date_message.todayTimeS) == 35 and is_true == 0:
                is_true = 1
                jjambab_message.reload_jjambab()
                title, description = jjambab_message.result_jjambab("점심")
                await channel.send(embed=set_embed(title, description))
                is_true = 0
            if int(date_message.todayTimeH) == 17 and int(date_message.todayTimeM) == 0 and int(date_message.todayTimeS) == 5 and is_true == 0:
                is_true = 1
                await channel.send(embed=set_embed("밥시간 알림", "저녁 30분전 입니다"))
                is_true = 0
            if int(date_message.todayTimeH) == 17 and int(date_message.todayTimeM) == 30 and int(date_message.todayTimeS) == 35 and is_true == 0:
                is_true = 1
                jjambab_message.reload_jjambab()
                title, description = jjambab_message.result_jjambab("저녁")
                await channel.send(embed=set_embed(title, description))
                is_true = 0
            if int(date_message.todayTimeH) == 20 and int(date_message.todayTimeM) == 0 and int(date_message.todayTimeS) == 5 and is_true == 0:
                is_true = 1
                await channel.send(embed=set_embed("청소시간 알림", " 개인임무분담제에 의한 청소 30분전 입니다"))
                is_true = 0
            if int(date_message.todayTimeH) == 20 and int(date_message.todayTimeM) == 30 and int(date_message.todayTimeS) == 5 and is_true == 0:
                is_true = 1
                await channel.send(embed=set_embed("청소시간 알림", " 개인임무분담제에 의한 청소를 해야합니다"))
                is_true = 0
        except:
            is_true = 0
        await asyncio.sleep(1)

#########################################################################
    
@client.event
async def on_message(message):

    #-----------------------------------------------------------------#
    if message.author == client.user:
        return
    #-----------------------------------------------------------------#
    
    if message.content.startswith("/?"):
        await message.channel.send(embed=set_embed("단결! 명령어를 불러드렸습니다!!", "/(오늘, 내일, 어제) 짬밥\n/(원하는 일자)일 짬밥\n/px\n/근무 추가\n/근무 보기\n/근무 삭제\n/검색 (원하는 검색어)\n/노래 (원하는 노래)"))
        
    #-----------------------------------------------------------------#
	
    search_day = ""
    
    last_text = message.content
    result_day = re.findall("\d+", last_text)
    for result in result_day:
        search_day = result
        
    if message.content == "/%s일 짬밥"%search_day:
        jjambab_message.reload_jjambab()
        title, description = jjambab_message.search_jjambab(search_day)
        await message.channel.send(embed=set_embed(title, description))
    
    if message.content.startswith("/오늘 짬밥"):
        jjambab_message.reload_jjambab()
        title, description = jjambab_message.result_jjambab("오늘")
        await message.channel.send(embed=set_embed(title, description))
        
    if message.content.startswith("/내일 짬밥"):
        jjambab_message.reload_jjambab()
        title, description = jjambab_message.result_jjambab("내일")
        await message.channel.send(embed=set_embed(title, description))
        
    if message.content.startswith("/어제 짬밥"):
        jjambab_message.reload_jjambab()
        title, description = jjambab_message.result_jjambab("어제")
        await message.channel.send(embed=set_embed(title, description))
        
    if message.content.startswith("/px"):
        title = "\n단결! px이용시간 입니다!!\n"
        description = "==========평일==========\n10:30 ~ 11:50\n13:00 ~ 17:00 \n 18:00 ~ 19:30\n==========휴일==========\n14:00 ~ 17:30\n========================"
        await message.channel.send("/tts " + title + description)
    
    #-----------------------------------------------------------------#
    
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
        
    #-----------------------------------------------------------------#
    
    if message.content == "/종료":
        todaySeconds = date_message.reload_today()
        title = "단결! 봇을 종료하겠습니다!!"
        description = "==========0초뒤 중료=========="
        await message.channel.send(embed=set_embed(title, description))
        scheduler_message.sched_stop()
        scheduler_message.sched_shutdown()
        await client.logout()
        
    #-----------------------------------------------------------------#
    
    if message.content.startswith("/검색"):
        last_text = message.content
        result_text_0 = last_text.replace("/검색 ","")
        result_text_1 = result_text_0.replace(" ","+")
        if result_text_1 == "/검색":
            title = "단결! 검색을 실패 하였습니다!!"
            description = "==========검색 실패==========\n예제 /검색 꺼무위키 꺼라"  + "\n==========================="
            await message.channel.send(embed=set_embed(title, description))
        else:
            google_site = "https://www.google.co.kr/search?q="
            naver_site = "https://search.naver.com/search.naver?query="
            youtube_site = "https://www.youtube.com/results?search_query="
            title = "단결! 검색을 완료 하였습니다!!"
            description = "==========검색 결과==========\n" + google_site + result_text_1 + "\n" + naver_site + result_text_1 + "\n==========================="
            await message.channel.send(embed=set_embed(title, description))  
            
    #-----------------------------------------------------------------#
    
    if message.content.startswith("/노래"):
        last_text = message.content
        result_text_0 = last_text.replace("/노래 ","")
        result_text_1 = result_text_0.replace(" ","+")
        if result_text_1 == "/노래":
            title = "단결! 노래 검색을 실패 하였습니다!!"
            description = "==========검색 실패==========\n예제 /노래 볼빨간사춘기 워커홀릭" + "\n==========================="
            await message.channel.send(embed=set_embed(title, description))
        else:
            youtube_site = "https://www.youtube.com/results?search_query="
            soundcloud_site = "https://soundcloud.com/search?q="
            title = "단결! 노래 검색을 완료 하였습니다!!"
            description = "==========검색 결과==========\n" + youtube_site + result_text_1 + "\n" + soundcloud_site + result_text_1 + "\n==========================="
            await message.channel.send(embed=set_embed(title, description))
            
    #-----------------------------------------------------------------#
    
    if message.content.startswith("/롤"):
        last_text = message.content
        result_text_0 = last_text.replace("/롤 ","")
        result_text_1 = result_text_0.replace(" ","+")
        if result_text_1 == "/롤":
            title = "단결! 롤 전적 검색을 실패 하였습니다!!"
            description = "==========검색 실패==========\n예제 /롤 명돌이0" + "\n==========================="
            await message.channel.send(embed=set_embed(title, description))
        else:
            opgg_site = "https://www.op.gg/summoner/userName="
            title = "단결! 롤 전적 검색을 완료 하였습니다!!"
            description = "==========검색 결과==========\n" + opgg_site + result_text_1 + "\n==========================="
            await message.channel.send(embed=set_embed(title, description))
            
    #-----------------------------------------------------------------#
    
    name = ""
    date_0 = ""
    date_1 = ""
    result_date = ""
    percent = ""
    
    if message.content == "/전역":
        title, description = calculator_message.result_calculator("전역")
        await message.channel.send(embed=set_embed(title, description))
    
    last_text = message.content
    result_text = re.findall("\w+", last_text)
    result_len = len(result_text)

    if message.content.startswith("/전역 추가"):
        if result_len == 9:
            name = result_text[2]
            date_0 = str(result_text[3]) + "." + str(result_text[4]) + "." + str(result_text[5])
            date_1 = str(result_text[6]) + "." + str(result_text[7]) + "." + str(result_text[8])
        else:
            return
        
    if message.content == "/전역 추가 %s,%s,%s"%(name,date_0,date_1):
        last_index = calculator_message.last_index()
        result_date_0 = re.findall("\d", date_0)
        search_date_0 = []
        search_date_0.append(str(result_date_0[0]) + str(result_date_0[1]) + str(result_date_0[2]) + str(result_date_0[3]))
        search_date_0.append(str(result_date_0[4]) + str(result_date_0[5]))
        search_date_0.append(str(result_date_0[6]) + str(result_date_0[7]))
        other_0 = date_message.other_date(int(search_date_0[0]),int(search_date_0[1]),int(search_date_0[2]))
        result_date_1 = re.findall("\d", date_1)
        search_date_1 = []
        search_date_1.append(str(result_date_1[0]) + str(result_date_1[1]) + str(result_date_1[2]) + str(result_date_1[3]))
        search_date_1.append(str(result_date_1[4]) + str(result_date_1[5]))
        search_date_1.append(str(result_date_1[6]) + str(result_date_1[7]))
        other_1 = date_message.other_date(int(search_date_1[0]),int(search_date_1[1]),int(search_date_1[2]))

        other_2 = date_message.other_date(int(date_message.todayY),int(date_message.todayM),int(date_message.todayD))
        all_day = date_message.reduce_date(other_1,other_0)
        reduce_day = date_message.reduce_date(other_1,other_2)
        result_day = ((all_day - reduce_day) / all_day) * 100
        percent_day = str(round(result_day,2)) + "%"
        #print(percent_day)
        calculator_message.calculator_write(name,date_0,date_1,"","",last_index+1)
        title, description = calculator_message.result_calculator("전역 추가")
        await message.channel.send(embed=set_embed(title, description))
        
    test = ""
    
    if message.content == "/전역 보기":
        last_index = calculator_message.last_index()
        name,date_0,date_1,result_date,percent = calculator_message.calculator_all_load()
        title, description = calculator_message.result_calculator("전역 보기")
        test = "이름 | 전역일 | 입대일 | 일자 | 퍼센트"
        test += "\n---------------------------------------------------------------------------"
        for i in range(0,last_index-1):
            text = "\n" + name[i] + " | " + date_1[i] + " | " + date_0[i] + " | " + result_date[i] + " | " + percent[i]
            test += text
            test += "\n---------------------------------------------------------------------------"
        test += "\n"
        #print(test)
        await message.channel.send(embed=set_embed(title, test))
    
    if message.content == "/전역 삭제":
        last_index = calculator_message.last_index()
        if last_index <= 2:
            title, description = calculator_message.result_calculator("전역 삭제 실패")
            await message.channel.send(embed=set_embed(title, test))
        else:
            calculator_message.calculator_delete(last_index)
            title, description = calculator_message.result_calculator("전역 삭제")
            await message.channel.send(embed=set_embed(title, test))
	#-----------------------------------------------------------------#
	
    #if message.content == "/자동 시작":
        #await message.channel.send(embed=set_embed("시작","합니다"))
        #scheduler_message.sched_start()
    	
    if message.content == "/시간":
        test = ""
        test += date_message.todayY + "년 /"
        test += date_message.todayM + "월 /"
        test += date_message.yesterdayD + "어제 /"
        test += date_message.todayD + "오늘 /"
        test += date_message.tomorrowD + "내일 /"
        test += date_message.todayTimeH + ":"
        test += date_message.todayTimeM + ":"
        test += date_message.todayTimeS
        await message.channel.send(embed=set_embed("시간",test))

#########################################################################

client.run("NjIwMTM3NTY0ODQxNTc0NDIx.Xb0ipw.rLzRh6A90AueSFyD8jRH7v1sohY")
