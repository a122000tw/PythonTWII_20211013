import requests
from datetime import date, timedelta


def getData():
    url = 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=20211103&selectType=ALL'
    start_date = date(2021, 10, 1)
    end_date = date(2021, 11, 3)
    delta = timedelta(days=1)
    while start_date <= end_date:
        url = url.replace(url[66:74], start_date.strftime("%Y%m%d"))
        print(url, start_date)
        start_date += delta

# def getData(yyyy, mm, dd):
#     yyyymmdd = str(yyyy) + str(mm) + str(dd)
#     url = 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=yyyymmdd&selectType=ALL' % yyyymmdd
#     url = url.replace(url[66:73], yyyymmdd)
#
#     print(url)


getData()

