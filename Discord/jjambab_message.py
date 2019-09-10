#---------------------#
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
#---------------------#
import date_message
#---------------------#

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

testSheets = ServiceAccountCredentials.from_json_keyfile_name("testSheets.json", scope)

clients = gspread.authorize(testSheets)

sheet = clients.open("2019-09 jjambab").sheet1

data = sheet.get_all_records()

#cell = sheet.cell(1,2).value
todayD = int(date_message.todayD)
todayM = int(date_message.todayM)
tomorrowD = int(date_message.tomorrowD)
yesterdayD= int(date_message.yesterdayD)

for i in range(0, 32):
    
    if i == todayD:
            today_breakfast = sheet.cell(todayD + 1,2).value
            today_lunch = sheet.cell(todayD + 1, 3).value
            today_dinner = sheet.cell(todayD + 1, 4).value
            
    if i == tomorrowD:
            tomorrow_breakfast = sheet.cell(tomorrowD + 1,2).value
            tomorrow_lunch = sheet.cell(tomorrowD + 1, 3).value
            tomorrow_dinner = sheet.cell(tomorrowD + 1, 4).value
            
    if i == yesterdayD:
            yesterday_breakfast = sheet.cell(yesterdayD + 1,2).value
            yesterday_lunch = sheet.cell(yesterdayD + 1, 3).value
            yesterday_dinner = sheet.cell(yesterdayD + 1, 4).value
            
today_result = str(todayM) + "월" + str(todayD) + "일" + " 짬밥입니다\n" + "==========아침==========\n" + today_breakfast + "\n==========점심==========\n" + today_lunch + "\n==========저녁==========\n" + today_dinner + "\n========================"

print(today_result)