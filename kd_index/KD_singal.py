import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # 顯示所有欄位
    pd.set_option('display.max_columns', None)
    # 顯示所有列
    pd.set_option('display.max_rows', None)
    # 設定列表寬度
    pd.set_option('display.width', 500)
    # 設定資料庫路徑
    db_path = '../每日股價/財經資料庫.db'
    conn = sqlite3.connect(db_path)
    # 查找某一檔股票(0050)最近幾天(450天)的紀錄
    sql = '''
        SELECT strftime('%Y%m%d', date) as date, 開盤價, 最高價, 最低價, 收盤價 FROM price
        WHERE stock_id = '2317' AND strftime('%Y%m%d', date) in (SELECT DISTINCT(strftime('%Y%m%d', date)) as date FROM price ORDER by date DESC LIMIT 488)
    '''
    # print(sql)
    # 將資料讀進到 pd.DataFrame
    tx = pd.read_sql(sql, conn)
    tx = tx.set_index('date')
    # print(tx)
    print('------------------------------------------------------------------------')
    # RSV = (今日收盤價 - 最近9天的最低價) / (最近9天的最高價 - 最近9天的最低價)
    # 計算 9 日 內的最高成交價
    tx['9dMax'] = tx['最高價'].rolling(9).max()
    # 計算 9 日 內的最低成交價
    tx['9dMin'] = tx['最低價'].rolling(9).min()
    # 刪除 NaN 資料列
    tx = tx.dropna()
    # print(tx)
    print('-------------------------------------------------------------------------')
    tx['RSV'] = 0
    tx['RSV'] = 100 * (tx['收盤價'] - tx['9dMin']) / (tx['9dMax'] - tx['9dMin'])
    # print(tx)
    print('-------------------------------------------------------------------------')
    # apply() 的使用
    # def add(n):
    #     return n + 3
    # df = pd.DataFrame({'x':[1, 2, 3], 'y':[4, 5, 6]})
    # print(df)
    # df['new_y'] = df['y'].apply(add)
    # print(df)
    print('-------------------------------------------------------------------------')
    # 計算 K 值
    # K 是 RSV 和前一日 K 值的加權平均
    # k = 2/3 * (昨日 K 值) + 1/3 * (今日 RSV)
    K = 0
    def KValue(rsv):
        global K
        K = (2/3) * K + (1/3) * rsv
        return K
    tx['K'] = 0
    tx['K'] = tx['RSV'].apply(KValue)
    # print(tx)
    print('-------------------------------------------------------------------------')
    # 計算 D 值
    # D 是 K 值和前一日 D 值的加權平均
    # D = 2/3 * (昨日 D 值) + 1/3 * (今日 K)
    D = 0
    def DValue(K):
        global D
        D = (2 / 3) * D + (1 / 3) * K
        return D
    tx['D'] = 0
    tx['D'] = tx['K'].apply(DValue)
    print(tx)
    print('-------------------------------------------------------------------------')
    # 買賣訊號
    # 黃金交叉買進訊號 / 死亡交叉賣出訊號
    # 今天 k > d 昨天 k < d  /  今天 k < d 昨天 k > d
    # 判斷市場行情一般都是使用 D 值 的數據
    # D > 80: 超買區 D < 20: 超賣區
    # D = 50: 多空平衡
    # D > 50: 多頭占上風
    # D < 50: 空頭占上風
    k = tx['K']
    d = tx['D']
    close = tx['收盤價']
    buy = (k > d) & (k.shift() < d.shift()) & (d < 20)
    sale = (k < d) & (k.shift() > d.shift()) & (d > 80)
    # print(sale)
    # print(buy)
    filter = buy == True
    filter2 = sale == True
    print(buy[filter])
    print(sale[filter2])
    # 報酬率
    count = 0
    cost = 0
    amount = 1000
    for i, v in buy.items():
        if v == True:
            print('日期', i, '訊號:', v, '收盤價:', tx.loc[i]['收盤價'])
            cost = cost + (tx.loc[i]['收盤價'] * amount)
            count = count + 1

    # 今日收盤價
    price = tx.iloc[-1]['收盤價']
    print('今日收盤價:', price)
    bal = count * amount * price
    print('cost:', cost, 'count:', count, 'bal:', bal, bal - cost, '報酬率:', (bal - cost) / cost)
    # 繪圖
    # k.plot(label="K", color='orange')
    # d.plot(label="D", color='blue')
    buy = buy.astype(int)
    sale = sale.astype(int)
    close.plot(label="close", color='gray')
    buy.plot(secondary_y=True, label='buy', color='red')
    sale.plot(secondary_y=True, label='sale', color='green')
    plt.legend()
    plt.show()

