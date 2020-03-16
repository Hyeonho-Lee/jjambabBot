import os
import re
import time
import datetime
import requests
from bs4 import BeautifulSoup as bs

def get_weather():
    place = '법원읍+날씨'
    site = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query={place}'.format(place = place)

    req = requests.get(site)
    soup = bs(req.content, 'html.parser')

    weather_0 = soup.find_all('span', class_='todaytemp')
    today_weather_0 = weather_0[0].text
    tomorrow_weather_0 = weather_0[1].text
    tomorrow_weather_1 = weather_0[2].text

    weather_1 = soup.find_all('p', class_='cast_txt')
    today_weather_1 = weather_1[0].text
    tomorrow_weather_2 = weather_1[1].text
    tomorrow_weather_3 = weather_1[2].text

    weather_2 = soup.find_all('span', class_='num')
    tomorrow_weather_4 = weather_2[9].text
    tomorrow_weather_5 = weather_2[10].text

    today_weather = '오늘 법원읍 날씨입니다.\n오늘 날씨는 [온도 = {today_weather_0}℃] 이며\n구름은 {today_weather_1}.'.format(today_weather_0 = today_weather_0, today_weather_1 = today_weather_1)
    tomorrow_weather = '내일 법원읍 날씨입니다.\n오전 [온도 = {tomorrow_weather_0}℃], [구름 = {tomorrow_weather_2}], [강수량 = {tomorrow_weather_4}%] 이며\n오후 [온도 = {tomorrow_weather_1}℃], [구름 = {tomorrow_weather_3}], [강수량 = {tomorrow_weather_5}%] 입니다.'.format(tomorrow_weather_0 = tomorrow_weather_0, tomorrow_weather_2 = tomorrow_weather_2, tomorrow_weather_4 = tomorrow_weather_4, tomorrow_weather_1 = tomorrow_weather_1, tomorrow_weather_3 = tomorrow_weather_3, tomorrow_weather_5 = tomorrow_weather_5)
    return today_weather, tomorrow_weather

#today_weather, tomorrow_weather = get_weather()
#print(today_weather, tomorrow_weather)
