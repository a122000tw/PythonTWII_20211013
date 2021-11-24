import requests
import pandas as pd
import io
date = '20120101'
url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=%s&type=ALLBUT0999&_=1637313358178' % date
r = requests.get(url)
lines = r.text.split('\n')
print(len(lines))
print(len(lines[0].split('",')))
print(len(lines[100].split('",')))
print(len(lines[800].split('",')))
print(len(lines[900].split('",')))
