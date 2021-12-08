import requests
import pandas as pd
import io
import sqlite3

date = '2021-12-07'


url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=%s&type=ALLBUT0999&_=1637313358178' % (date.replace("-", ""))
r = requests.get(url)
lines = r.text.split('\n')
print(r)
newlines = []
for line in lines:
    if(len(line.split('",')) == 17):
        newlines.append(line)
#  將 line 轉為 dataframe
data = '\n'.join(newlines).replace('=', '')
df = pd.read_csv(io.StringIO(data))
df = df.astype(str)
df = df.apply(lambda s: s.str.replace(',', ''))
# 加入日期
df['date'] = date
df['stock_id'] = df['證券代號']
df = df.drop('證券代號', axis=1)
df = df.set_index(['stock_id', 'date'])
df = df.apply(lambda s: pd.to_numeric(s, errors='coerce'))
df = df.dropna(axis=1, how='all')
print(df)
# ---------------------------------------------------------------
# 先存成 csv 再轉存 sqlite
df.to_csv('price.csv', encoding='utf_8')
# 轉存 sqlite3
conn = sqlite3.connect('../../database/財經資料庫.db')
# df.to_sql('price', conn, if_exists='replace')
df.to_sql('price', conn, if_exists='append')




