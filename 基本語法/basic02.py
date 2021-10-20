import math
if __name__ == '__main__':
    r = 123
    # 求出園面積與球體積 (利用 math api 取得圓周率)
    # 請印出結果小數點到第二位
    s = r**2*math.pi
    v = 4/3*math.pi*(r**3)
    print('圓面積=%.2f' % s, '球的體積=%.2f' % v)
