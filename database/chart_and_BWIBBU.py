import sqlite3
import matplotlib.pyplot as plt

symbol = '2317'
kind = 'yield'
conn = sqlite3.connect('tw_stock.db')
cursor = conn.cursor()
# sql = "select ts, pe from BWIBBU where symbol='%s'" % symbol
sql = 'select strftime("%Y-%m", ts) as "ts", ROUND(AVG('+kind+'), 2) as "'+kind+'" ' \
      'from BWIBBU  ' \
      'where symbol="'+symbol+'" ' \
      'group by strftime("%Y-%m", ts)'

cursor.execute(sql)
datas = cursor.fetchall()
print(datas)
# 繪圖前準備
x_datas = []  # x 軸(時間序列)
y_datas = []  # y 軸(本益比)
for data in datas:
    x_datas.append(data[0])
    y_datas.append(data[1])
print(x_datas)
print(y_datas)
# 繪圖
plt.plot_date(x_datas, y_datas, '-')
plt.title('%s Stock Info' % symbol)
plt.xlabel('date')
plt.ylabel('PE')
plt.grid(True)
plt.show()

