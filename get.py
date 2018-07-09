# -*- coding: utf-8 -*-

import requests
import datetime
import sys
import re

from bs4 import BeautifulSoup

urls = [
    'https://www.daily-zodiac.com/mobile/zodiac/Aries',       # 牡羊
    'https://www.daily-zodiac.com/mobile/zodiac/Taurus',      # 金牛
    'https://www.daily-zodiac.com/mobile/zodiac/Gemini',      # 雙子
    'https://www.daily-zodiac.com/mobile/zodiac/Cancer',      # 巨蟹
    'https://www.daily-zodiac.com/mobile/zodiac/Leo',         # 獅子
    'https://www.daily-zodiac.com/mobile/zodiac/Virgo',       # 處女
    'https://www.daily-zodiac.com/mobile/zodiac/Libra',       # 天秤
    'https://www.daily-zodiac.com/mobile/zodiac/Scorpio',     # 天蠍
    'https://www.daily-zodiac.com/mobile/zodiac/Sagittarius', # 射手
    'https://www.daily-zodiac.com/mobile/zodiac/Capricorn',   # 魔羯
    'https://www.daily-zodiac.com/mobile/zodiac/Aquarius',    # 水平
    'https://www.daily-zodiac.com/mobile/zodiac/Pisces',      # 雙魚
    ]

now = datetime.date.today()
filename = str(now.year)+str(now.month).zfill(2)+str(now.day).zfill(2)+'.txt'
print ('建立今日運勢檔案：'+filename)
fp = open(filename, 'w')

print ('開始抓運勢囉！')
for url in urls :
    resp = requests.get(url)
    page = resp.text
    soup = BeautifulSoup(page, 'html.parser')
    name = soup.find('p', class_='name').text
    today = soup.find('ul', class_='today').findAll('li')

    print('正在抓 '+name)
    fp.write(name+'\n')
    msg1 = today[0].text + ' ' + today[1].text + ' ' + today[2].text.replace('\n', '')
    fp.write(msg1+'\n')
    article = soup.find('article').text.strip()
    fp.write(article+'\n\n')
print ('抓完了，打開 ' + filename + ' 複製吧！')

fp.close()
