from random import random
times=int(input("请输入掷飞镖的次数："))
hits=0
for i in range(times):
    x=random()
    y=random()
    if x*x+y*y<=1:
        hits+=1
print('击中次数',hits)
print('圆周率近似值',4.0*hits/times)