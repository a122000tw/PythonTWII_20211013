import sqlite3

conn = sqlite3.connect('tw_stock.db')
cursor = conn.cursor()
sql = "insert into portfolio(symbol, cost, amount, ts) " \
      "values(?, ?, ?, ?)"

# list 內容一定是 Tuple
datas = [('2303', 50, 7000, '2021-11-03'),
         ('2317', 110, 6000, '2021-11-03'),
         ('2498', 70.5, 4000, '2021-11-03')]
# 批次新增
cursor.executemany(sql, datas)
conn.commit()
conn.close()
