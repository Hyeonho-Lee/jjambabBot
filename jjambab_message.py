#---------------------#
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
#---------------------#
import date_message
#---------------------#

date_message.reload_today()

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

testSheets = ServiceAccountCredentials.from_json_keyfile_name("testSheets.json", scope)

clients = gspread.authorize(testSheets)
sheet = clients.open("2019-10 jjambab").sheet1
    
data = sheet.get_all_records()

for i in range(0, 32):

    if i == int(date_message.todayD):
        today_breakfast = sheet.cell(int(date_message.todayD) + 1,2).value
        today_lunch = sheet.cell(int(date_message.todayD) + 1, 3).value
        today_dinner = sheet.cell(int(date_message.todayD) + 1, 4).value

    if i == int(date_message.tomorrowD):
        tomorrow_breakfast = sheet.cell(int(date_message.tomorrowD) + 1,2).value
        tomorrow_lunch = sheet.cell(int(date_message.tomorrowD) + 1, 3).value
        tomorrow_dinner = sheet.cell(int(date_message.tomorrowD) + 1, 4).value

    if i == int(date_message.yesterdayD):
        yesterday_breakfast = sheet.cell(int(date_message.yesterdayD) + 1,2).value
        yesterday_lunch = sheet.cell(int(date_message.yesterdayD) + 1, 3).value
        yesterday_dinner = sheet.cell(int(date_message.yesterdayD) + 1, 4).value
        
def reload_jjambab():
    
    date_message.reload_today()
    
    for i in range(0, 32):

        if i == int(date_message.todayD):
            today_breakfast = sheet.cell(int(date_message.todayD) + 1,2).value
            today_lunch = sheet.cell(int(date_message.todayD) + 1, 3).value
            today_dinner = sheet.cell(int(date_message.todayD) + 1, 4).value

        if i == int(date_message.tomorrowD):
            tomorrow_breakfast = sheet.cell(int(date_message.tomorrowD) + 1,2).value
            tomorrow_lunch = sheet.cell(int(date_message.tomorrowD) + 1, 3).value
            tomorrow_dinner = sheet.cell(int(date_message.tomorrowD) + 1, 4).value

        if i == int(date_message.yesterdayD):
            yesterday_breakfast = sheet.cell(int(date_message.yesterdayD) + 1,2).value
            yesterday_lunch = sheet.cell(int(date_message.yesterdayD) + 1, 3).value
            yesterday_dinner = sheet.cell(int(date_message.yesterdayD) + 1, 4).value
                
def search_jjambab(result):
    date_message.reload_today()
    reload_jjambab()
    search = int(result)
    search_breakfast = sheet.cell(search + 1,2).value
    search_lunch = sheet.cell(search + 1, 3).value
    search_dinner = sheet.cell(search + 1, 4).value
    search_result = "단결! " + str(date_message.todayM) + "월" + str(search) + "일" + " 짬밥입니다!!\n"
    searchs_result = "==========아침==========\n" + search_breakfast + "\n==========점심==========\n" + search_lunch + "\n==========저녁==========\n" + search_dinner + "\n========================"
    return search_result, searchs_result

def result_jjambab(result):
    date_message.reload_today()
    reload_jjambab()
    if result == "오늘":
        title = "단결! " + str(date_message.todayM) + "월" + str(date_message.todayD) + "일" + " 짬밥입니다!!\n"
        description = "==========아침==========\n" + today_breakfast + "\n==========점심==========\n" + today_lunch + "\n==========저녁==========\n" + today_dinner + "\n========================"
    elif result == "내일":
        title = "단결! " + str(date_message.todayM) + "월" + str(date_message.tomorrowD) + "일" + " 짬밥입니다!!\n"
        description = "==========아침==========\n" + tomorrow_breakfast + "\n==========점심==========\n" + tomorrow_lunch + "\n==========저녁==========\n" + tomorrow_dinner + "\n========================"
    elif result == "어제":
        title = "단결! " + str(date_message.todayM) + "월" + str(date_message.yesterdayD) + "일" + " 짬밥입니다!!\n"
        description = "==========아침==========\n" + yesterday_breakfast + "\n==========점심==========\n" + yesterday_lunch + "\n==========저녁==========\n" + yesterday_dinner + "\n========================"
    elif result == "아침":
        title = "단결! 오늘의 아침밥을 불러드렸습니다!"
        description = "==========아침==========\n" + today_breakfast + "\n========================"
    elif result == "점심":
        title = "단결! 오늘의 점심밥을 불러드렸습니다!"
        description = "==========점심==========\n" + today_lunch + "\n========================"
    elif result == "저녁":
        title = "단결! 오늘의 저녁밥을 불러드렸습니다!"
        description = "==========저녁==========\n" + today_dinner + "\n========================"
    return title, description

