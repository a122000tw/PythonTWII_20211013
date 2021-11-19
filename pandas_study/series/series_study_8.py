import pandas as pd

print(pd.__version__)
# 綜合練習 Series 1
# 請求出 s.rolling(2).sum().cumsum() + 1 找出最大值
s = pd.Series([1, 2, 3, 4, 5], index=pd.date_range('20211101', periods=5))
print(s)
a = s.rolling(2).sum()
b = a.cumsum()
c = b + 1
d = c.max()
print(a)
print(b)
print(c)
print(d)

