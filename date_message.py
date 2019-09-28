#---------------------#
import pytz
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
#---------------------#

KRT = pytz.timezone('Asia/Seoul')
KR_sloct = KRT.localize(datetime.datetime.now())

todayD = KR_sloct.strftime('%d')
todayM = KR_sloct.strftime('%m')
#todayDate = today.strftime('%Y-%m-%d')
todayTime = KR_sloct.strftime('%H:%M:%S')

todays = KR_sloct.strftime('오늘은 %m월 %d일 입니다.')
todayT = str(KR_sloct.year) + "년 " + str(KR_sloct.month) + "월 " + str(KR_sloct.day) + "일"
tomorrow = KR_sloct + datetime.timedelta(days=1)
tomorrows = tomorrow.strftime('내일은 %m월 %d일 입니다.')
tomorrowD = tomorrow.strftime('%d')

yesterday = KR_sloct - datetime.timedelta(days=1)
yesterdays = yesterday.strftime('어제는 %m월 %d일 입니다.')
yesterdayD = yesterday.strftime('%d')

#"""
def reload_today():
    KRT = pytz.timezone('Asia/Seoul')
    KR_sloct = KRT.localize(datetime.datetime.now())

    todayD = KR_sloct.strftime('%d')
    todayM = KR_sloct.strftime('%m')
    #todayDate = today.strftime('%Y-%m-%d')
    todayTime = KR_sloct.strftime('%H:%M:%S')

    todays = KR_sloct.strftime('오늘은 %m월 %d일 입니다.')
    todayT = str(KR_sloct.year) + "년 " + str(KR_sloct.month) + "월 " + str(KR_sloct.day) + "일"
    tomorrow = KR_sloct + datetime.timedelta(days=1)
    tomorrows = tomorrow.strftime('내일은 %m월 %d일 입니다.')
    tomorrowD = tomorrow.strftime('%d')

    yesterday = KR_sloct - datetime.timedelta(days=1)
    yesterdays = yesterday.strftime('어제는 %m월 %d일 입니다.')
    yesterdayD = yesterday.strftime('%d')
    
    print(KR_sloct)

#def exec_cron():
    #print("hi")
    
#sched = BlockingScheduler()
#sched.add_job(exec_interval, 'interval', seconds=10)
#sched.add_job(exec_cron, 'cron', minute='*/1', second='10, 30')
#sched.start()
#"""
