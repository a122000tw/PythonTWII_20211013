import requests
import pandas as pd
import io
import sqlite3
from datetime import date, datetime, timedelta
import time


today = date.today()
begin_day = date(2011, 9, 2)
# print(today, begin_day)
diff = today - begin_day
# print(diff)

for single_date in (begin_day + timedelta(n) for n in range(diff.days+1)):
    date = str(single_date)
    print(date)

    url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=%s&type=ALLBUT0999&_=1637313358178' % (
        date.replace("-", ""))
    r = requests.get(url)
    lines = r.text.split('\n')
    newlines = []

    if len(lines) == 1:
        continue
    else:
        for line in lines:
            if (len(line.split('",')) == 17):
                newlines.append(line)

        #  將 line 轉為 dataframe
        data = '\n'.join(newlines).replace('=', '')
        df = pd.read_csv(io.StringIO(data))
        df = df.astype(str)
        df = df.apply(lambda s: s.str.replace(',', ''))
        # 加入日期
        df['交易日'] = date
        df = df.set_index('證券代號', '交易日')
        df = df.apply(lambda s: pd.to_numeric(s, errors='coerce'))
        df = df.dropna(axis=1, how='all')
        print(df)
        # ---------------------------------------------------------------
        # 先存成 csv 再轉存 sqlite
        df.to_csv('price.csv', encoding='utf_8')
        # 轉存 sqlite3
        conn = sqlite3.connect('財經資料庫.db')
        # df.to_sql('price', conn, if_exists='replace')
        df.to_sql('price', conn, if_exists='append')
        time.sleep(10)
        print('完成:', single_date)


print('全部完成')




