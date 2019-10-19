#---------------------#
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import os
import re
#---------------------#
import date_message
#---------------------#

date_message.reload_today()

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

testSheets = ServiceAccountCredentials.from_json_keyfile_name("testSheets.json", scope)

clients = gspread.authorize(testSheets)
sheet = clients.open("test_calculator").sheet1
    
data = sheet.get_all_records()

def calculator_load(row):
    result = sheet.row_values(row)
    name = sheet.cell(row, 1).value
    date_0 = sheet.cell(row, 2).value
    date_1 = sheet.cell(row, 3).value
    result_date = sheet.cell(row, 4).value
    percent = sheet.cell(row, 5).value
    return name,date_0,date_1,result_date,percent
    
def calculator_all_load():
    
    data = sheet.get_all_records()
    
    name = []
    date_0 = []
    date_1 = []
    result_date = []
    percent = []
    
    for all_data in data:
        test = str(all_data)
        load_text = re.findall("\w+", test)
        name.append(load_text[1])
        date_0.append(str(load_text[3]) + "." + str(load_text[4]) + "." + str(load_text[5]))
        date_1.append(str(load_text[7]) + "." + str(load_text[8]) + "." + str(load_text[9]))
        result_date.append(load_text[11])
        percent.append(load_text[13])
        
    return name,date_0,date_1,result_date,percent
        
def calculator_write(name, date_0, date_1, result_date, percent, row):
    sheet.insert_row([name, date_0, date_1, result_date, percent], row)
    data = sheet.get_all_records()
    
def calculator_delete(row):
    int_row = int(row)
    sheet.delete_row(int_row)
    data = sheet.get_all_records()

def last_index():
    i = 1
    data = sheet.get_all_records()
    for all_data in data:
        i = i + 1
    return i

def result_calculator(result):
    if result == "전역":
        title = "단결! 전역 명령어 입니다!!"
        description = "이름,입대일,전역일 순으로 적어 주시길 바랍니다"
    elif result == "전역 추가":
        title = "단결! 전역을 추가하였습니다!!"
        description = "==========추가 완료=========="
    elif result == "전역 보기":
        title = "단결! 현제 준비된 근무입니다!!"
        description = "==========준비된 근무=========="
    elif result == "전역 삭제":
        title = "단결! 마지막 근무를 삭제하였습니다!!"
        description = "==========삭제 완료=========="
    elif result == "전역 삭제 실패":
        title = "단결! 여기부터는 삭제불가입니다!!"
        description = "==========삭제 실패=========="
    return title, description

#print(calculator_all_load())
