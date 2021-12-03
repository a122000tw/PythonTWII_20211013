import requests
import pandas as pd
import io
date = '20211117'
url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=%s&type=ALLBUT0999&_=1637313358178' % date
r = requests.get(url)
lines = r.text.split('\n')
newlines = []
for line in lines:
    if(len(line.split('",')) == 17):
        newlines.append(line)
#  將 line 轉為 dataframe
data = '\n'.join(newlines).replace('=', '')
df = pd.read_csv(io.StringIO(data))
#  將資料轉為 str
df = df.astype(str)
#  將內容有 , 的去除
df = df.apply(lambda s: s.str.replace(',', ''))
#  將證券代號 設定為 index
df['date'] = date
df['stock_id'] = df['證券代號']
df = df.drop('證券代號', axis=1)
df = df.set_index(['stock_id', 'date'])

#  去除非數字的資料
df = df.apply(lambda s: pd.to_numeric(s, errors='coerce'))
df = df.dropna(axis=1, how='all')
# print(df)
# 顯示所有欄位/數列
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
#  查出收盤價比開盤價高出 8% 的股票
print(df[df['收盤價'] / df['開盤價'] > 1.08])



