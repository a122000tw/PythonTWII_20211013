import math

if __name__ == '__main__':
    r = 123
    # 求出圓面積與球體積 (利用 math api 取得圓周率)
    # 請印出結果小數點到第二位
    area = (r**2)*math.pi
    v = 4/3*math.pi*(r**3)
    print('圓面積=%.2f' % area, '球體積=%.2f' % v)
    # 若要加上千分位
    print(type(area))
    # area = format(area, ",")
    # print(area, type(area))
    print('%.2f' % area)
    print(format(float('%.2f' % area), ","))
