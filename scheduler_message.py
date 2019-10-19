#---------------------#
import os
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import JobLookupError
#---------------------#
import jjambab_message
import date_message
#---------------------#

sched = BackgroundScheduler()

def kill_scheduler(job_id):
	try:
		sched.remove_job(job_id)
	except JobLookupError as err:
		print("스케쥴러 종료를 실패 하였습니다: %s")%err
		return

def shutdown(self):
	sched.shutdown()

def exec_cron():
	now = date_message.reload_today()
	date_message.todayTimeH =  now.strftime('%H')
	date_message.todayTimeM = now.strftime('%M')
	date_message.todayTimeS = now.strftime('%S')
	date_message.todayD = now.strftime('%d')
	date_message.todayM = now.strftime('%m')
	date_message.tomorrowD = now.strftime('%d')
	date_message.yesterdayD = now.strftime('%d')
	auto_check()
	
def scheduler(type,job_id):
	if type == "exec_cron":
		sched.add_job(exec_cron,'cron',minute='*/1',second='*/1',id=job_id)

#---------------------------------------------------------------#	
def calendar(hour,minute,second,text):
    if int(date_message.todayTimeH) == hour and int(date_message.todayTimeM) == minute and int(date_message.todayTimeS) == second:
        print(text)

def auto_check():
    calendar(7,30,0,"아침 먹을시간임")
    calendar(12,30,0,"점심 먹을시간임")
    calendar(17,30,0,"저녘 먹을시간임")
    calendar(20,25,0,"청소할 시간 5분전임")

def start():
	scheduler("exec_cron","1")

def stop():
	kill_scheduler("1")

sched.start()
