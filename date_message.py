#---------------------#
import datetime
#---------------------#

today = datetime.datetime.now()
todayD = today.strftime('%d')
todayM = today.strftime('%m')
#todayDate = today.strftime('%Y-%m-%d')
#todayTime = today.strftime('%H:%M')

todays = today.strftime('오늘은 %m월 %d일 입니다.')
todayT = str(today.year) + "년 " + str(today.month) + "월 " + str(today.day) + "일"
tomorrow = today + datetime.timedelta(days=1)
tomorrows = tomorrow.strftime('내일은 %m월 %d일 입니다.')
tomorrowD = tomorrow.strftime('%d')

yesterday = today - datetime.timedelta(days=1)
yesterdays = yesterday.strftime('어제는 %m월 %d일 입니다.')
yesterdayD = yesterday.strftime('%d')

def reload_today():
    today = datetime.datetime.now()
    
print(todayT)
