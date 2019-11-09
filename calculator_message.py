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
sheet = clients.open("test_calculator").sheet1

def write_calculator():
    with open("./calculator.txt", 'w') as file:
        c_data = str(data)
        text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》{}]', '', c_data)
        #text = text.replace("\\n", "/")
        file.write(text)
    return text

data = sheet.get_all_records()
c_data = write_calculator()
    
def calculator_all_load():
    
    data = sheet.get_all_records()
    c_data = write_calculator()
    load_text = c_data.split()

    name = []
    date_0 = []
    date_1 = []
    result_date = []
    percent = []
	
    for i in range(1,int(len(load_text)),6):
        name.append(str(load_text[i]))
    for i in range(3,int(len(load_text)),6):
        date_0.append(str(load_text[i])[0:4] + "." + str(load_text[i])[4:6] + "." + str(load_text[i])[6:8])
    for i in range(5,int(len(load_text)),6):
        date_1.append(str(load_text[i])[0:4] + "." + str(load_text[i])[4:6] + "." + str(load_text[i])[6:8])

    for i in range(0,int(len(load_text)/6)):
        other_0 = date_message.other_date(int(str(date_0[i])[0:4]),int(str(date_0[i])[5:7]),int(str(date_0[i])[8:10]))
        other_1 = date_message.other_date(int(str(date_1[i])[0:4]),int(str(date_1[i])[5:7]),int(str(date_1[i])[8:10]))
        other_2 = date_message.other_date(int(date_message.todayY),int(date_message.todayM),int(date_message.todayD))
        all_day = date_message.reduce_date(other_1,other_0)
        reduce_day = date_message.reduce_date(other_1,other_2)
        result_day = ((all_day - reduce_day) / all_day) * 100
        percent_day = str(round(result_day,2)) + "%"
        result_date.append(str(reduce_day.days) + "일")
        percent.append(str(percent_day))
    
    return name,date_0,date_1,result_date,percent
        
def calculator_write(name, date_0, date_1, result_date, percent, row):
    sheet.insert_row([name, date_0, date_1, result_date, percent], row)
    data = sheet.get_all_records()
    
def calculator_delete(row):
    int_row = int(row)
    sheet.delete_row(int_row)
    data = sheet.get_all_records()
	
def calculator_update(name, date_0, date_1, result_date, percent, row):
    sheet.update_row([name, date_0, date_1, result_date, percent], row)
    data = sheet.get_all_records()

def last_index():
    data = sheet.get_all_records()
    load_text = c_data.split()
    i = int(len(load_text)/6) + 1
    return i

def result_calculator(result):
    if result == "전역":
        title = "단결! 전역 명령어 입니다!!"
        description = "이름,입대일,전역일 순으로 적어 주시길 바랍니다"
    elif result == "전역 추가":
        title = "단결! 전역을 추가하였습니다!!"
        description = "==========추가 완료=========="
    elif result == "전역 보기":
        title = "단결! 현제 남은 복무일수 입니다!!"
        description = "==========준비된 근무=========="
    elif result == "전역 삭제":
        title = "단결! 마지막 근무를 삭제하였습니다!!"
        description = "==========삭제 완료=========="
    elif result == "전역 삭제 실패":
        title = "단결! 여기부터는 삭제불가입니다!!"
        description = "==========삭제 실패=========="
    return title, description

#print(calculator_all_load())
