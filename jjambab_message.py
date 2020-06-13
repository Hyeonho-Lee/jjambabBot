#---------------------#
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import os
import re
import datetime
#---------------------#
import date_message
#---------------------#

date_message.reload_today()

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

testSheets = ServiceAccountCredentials.from_json_keyfile_name("testSheets.json", scope)

clients = gspread.authorize(testSheets)
sheet = clients.open("2020-06 jjambab").sheet1

def write_jjambab():
    with open("./jjambab_2020_06.txt", 'w+t') as file:
        j_data = str(data)
        text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》{}]', '', j_data)
        text = text.replace("\\n", "/")
        file.write(text)
    return text

data = sheet.get_all_records()
j_data = write_jjambab()

def last_index():
    load_text = j_data.split()
    i = int(len(load_text)/6) + 1
    return i

def test_reload():
    load_text = j_data.split()
    breakfast = []
    lunch = []
    dinner = []
	
    for i in range(1,int(len(load_text)),6):
        breakfast.append(str(load_text[i]))
    for i in range(3,int(len(load_text)),6):
        lunch.append(str(load_text[i]))
    for i in range(5,int(len(load_text)),6):
        dinner.append(str(load_text[i]))

    return breakfast,lunch,dinner
                
def search_jjambab(result):
    search = int(result)
    search_result = "단결! " + str(date_message.todayM) + "월" + str(search) + "일" + " 짬밥입니다!!\n"
    searchs_result = ""
    return search_result, searchs_result

def result_jjambab(result):
    if result == "오늘":
        title = "단결! " + str(date_message.todayM) + "월" + str(date_message.todayD) + "일" + " 짬밥입니다!!\n"
        description = ""
    if result == "내일":
        title = "단결! " + str(date_message.todayM) + "월" + str(date_message.tomorrowD) + "일" + " 짬밥입니다!!\n"
        description = ""
    if result == "어제":
        title = "단결! " + str(date_message.todayM) + "월" + str(date_message.yesterdayD) + "일" + " 짬밥입니다!!\n"
        description = ""
    if result == "아침":
        title = "단결! 오늘의 아침밥을 불러드렸습니다!"
        description = ""
    if result == "점심":
        title = "단결! 오늘의 점심밥을 불러드렸습니다!"
        description = ""
    if result == "저녁":
        title = "단결! 오늘의 저녁밥을 불러드렸습니다!"
        description = ""
    if result == "내일아침":
        title = "단결! 내일의 아침밥을 불러드렸습니다!"
        description = ""
    return title, description
