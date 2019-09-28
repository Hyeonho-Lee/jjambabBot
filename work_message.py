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
sheet = clients.open("test_work").sheet1
    
data = sheet.get_all_records()

def work_load(row):
    result = sheet.row_values(row)
    index = sheet.cell(row, 1).value
    date = sheet.cell(row, 2).value
    writer = sheet.cell(row, 3).value
    time = sheet.cell(row, 4).value
    content = sheet.cell(row, 5).value
    #for value in result:
    #    print(value)
    return index,date,writer,time,content
    
def work_all_load():
    
    data = sheet.get_all_records()
    
    index = []
    date = []
    writer = []
    time = []
    content = []
    
    for all_data in data:
        test = str(all_data)
        load_text = re.findall("\w+", test)
        load_text_len = len(load_text)
        index.append(load_text[1])
        date.append(load_text[3])
        writer.append(load_text[5])
        time.append(load_text[7])
        content.append(load_text[9])
        
    return index,date,writer,time,content
    
    #for all_data in data:
        #print('-'.join(all_data))
        #print("====================")
        
def work_write(index, date, writer, time, content, row):
    sheet.insert_row([index, date, writer, time, content], row)
    data = sheet.get_all_records()
    
def work_delete(row):
    int_row = int(row)
    sheet.delete_row(int_row)
    data = sheet.get_all_records()
    
#index, date, writer, time, content = work_load(3)
#print(date)

def last_index():
    i = 1
    data = sheet.get_all_records()
    for all_data in data:
        i = i + 1
    #print(i)
    return i

def result_work(result):
    if result == "근무":
        title = "단결! 근무명령어 입니다!!"
        description = "날짜,작성자,시간,내용 순으로 적어 주시길 바랍니다"
    elif result == "근무 추가":
        title = "단결! 근무를 추가하였습니다!!"
        description = "==========추가 완료=========="
    elif result == "근무 보기":
        title = "단결! 현제 준비된 근무입니다!!"
        description = "==========준비된 근무=========="
    elif result == "근무 삭제":
        title = "단결! 마지막 근무를 삭제하였습니다!!"
        description = "==========삭제 완료=========="
    elif result == "근무 삭제 실패":
        title = "단결! 여기부터는 삭제불가입니다!!"
        description = "==========삭제 실패=========="
    return title, description

#index,date,writer,time,content = work_all_load()
#print(index,date,writer,time,content)

#for all_data in data:
#    i = 1
#    index = sheet.cell(i, 1).value
#    date = sheet.cell(i, 2).value
#    writer = sheet.cell(i, 3).value
#    time = sheet.cell(i, 4).value
#    content = sheet.cell(i, 5).value
    
#work_delete(5)

#test = sheet.cell(2, 2).value
#test1 = sheet.row_values(3)
#print(test1)


