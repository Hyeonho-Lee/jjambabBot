#---------------------#
import pytz
import datetime
#---------------------#

KRT = pytz.timezone('Asia/Seoul')
KR_sloct = KRT.localize(datetime.datetime.now())

todayD = KR_sloct.strftime('%d')
todayM = KR_sloct.strftime('%m')
todayY = KR_sloct.strftime('%Y')
todayDate = KR_sloct.strftime('%Y-%m-%d')
todayTime = KR_sloct.strftime('%H:%M:%S')
todayTimeS = KR_sloct.strftime('%S')
todayTimeM = KR_sloct.strftime('%M')
todayTimeH = KR_sloct.strftime('%H')

todays = KR_sloct.strftime('오늘은 %m월 %d일 입니다.')
todayT = todayY + "년 " + todayM + "월 " + todayD + "일"
tomorrow = KR_sloct + datetime.timedelta(days=1)
tomorrows = tomorrow.strftime('내일은 %m월 %d일 입니다.')
tomorrowD = tomorrow.strftime('%d')

yesterday = KR_sloct - datetime.timedelta(days=1)
yesterdays = yesterday.strftime('어제는 %m월 %d일 입니다.')
yesterdayD = yesterday.strftime('%d')

#"""
def reload_today():
    KRT = pytz.timezone('Asia/Seoul')
    KR = KRT.localize(datetime.datetime.now())
    KR_sloct = KR + datetime.timedelta(hours=9)
	
    todayD = KR_sloct.strftime('%d')
    todayM = KR_sloct.strftime('%m')
    todayY = KR_sloct.strftime('%Y')
    todayDate = KR_sloct.strftime('%Y-%m-%d')
    todayTime = KR_sloct.strftime('%H:%M:%S')
    todayTimeS = KR_sloct.strftime('%S')
    todayTimeM = KR_sloct.strftime('%M')
    todayTimeH = KR_sloct.strftime('%H')

    todays = KR_sloct.strftime('오늘은 %m월 %d일 입니다.')
    todayT = todayY + "년 " + todayM + "월 " + todayD + "일"
    tomorrow = KR_sloct + datetime.timedelta(days=1)
    tomorrows = tomorrow.strftime('내일은 %m월 %d일 입니다.')
    tomorrowD = tomorrow.strftime('%d')

    yesterday = KR_sloct - datetime.timedelta(days=1)
    yesterdays = yesterday.strftime('어제는 %m월 %d일 입니다.')
    yesterdayD = yesterday.strftime('%d')
    
    return KR_sloct

def reload_other():
    KRT = pytz.timezone('Asia/Seoul')
    sloct = KRT.localize(datetime.datetime.now())
    return sloct

def other_date(year,month,date):
    KRT = pytz.timezone('Asia/Seoul')
    other = KRT.localize(datetime.datetime(year, month, date))
    return other

def reduce_date(original, reduce):
    result = original - reduce
    return result
