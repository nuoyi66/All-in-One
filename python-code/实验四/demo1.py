x=int(input("请输入x："))
if x<0 or x>=20:
    y=0
elif x<5:
    y=x
elif x<10:
    y=3*x-5
elif x<20:
    y=0.5*x-2
print('y=',y)
