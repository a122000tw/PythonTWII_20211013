import sqlite3
import matplotlib.pyplot as plt


conn = sqlite3.connect('../../database/tw_stock.db')
cursor = conn.cursor()
symbol = '2330'
kind = 'yield'
sql = "select ts, pe, yield from BWIBBU where symbol='%s'" % symbol


cursor.execute(sql)
datas = cursor.fetchall()
print(datas)
# 繪圖前準備
x_datas = []  # x 軸(時間序列)
y_datas = []  # y 軸(本益比)
y2_datas = []  # y2 軸(yield)

for data in datas:
    x_datas.append(data[0])
    y_datas.append(data[1])
    y2_datas.append(data[2])
print(x_datas)
print(y_datas)
print(y2_datas)
# 繪圖
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
plt.title('%s Stock Info' % symbol)
plt.xlabel('date')
# 第一條線
ax1.set_ylabel('pe', color='tab:blue')
ax1.plot_date(x_datas, y_datas, '-')
# 第一條線
ax2.set_ylabel('pe', color='tab:orange')
ax2.plot_date(x_datas, y2_datas, '-', color="orange")
plt.show()
