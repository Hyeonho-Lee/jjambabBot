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
sheet = clients.open("2019-11 jjambab").sheet1
    
data = sheet.get_all_records()

def last_index():
    i = 1
    data = sheet.get_all_records()
    for all_data in data:
        i = i + 1
    return i

def test_reload():
    data = sheet.get_all_records()
    breakfast = []
    lunch = []
    dinner = []

    for all_data in data:
        test = str(all_data)
        text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》{}]', '', test)
        text = text.replace("\\n", "/")
        load_text = text.split()

        breakfast.append(str(load_text[1]))
        lunch.append(str(load_text[3]))
        dinner.append(str(load_text[5]))

    return breakfast,lunch,dinner
                
def search_jjambab(result):
    date_message.reload_today()
    search = int(result)
    search_result = "단결! " + str(date_message.todayM) + "월" + str(search) + "일" + " 짬밥입니다!!\n"
    searchs_result = ""
    return search_result, searchs_result

def result_jjambab(result):
    date_message.reload_today()
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
    return title, description
