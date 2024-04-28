def leapyear(year):
    if year%400==0 or year%4==0 and year%100!=0:
        return 1
    else:
        return 0
year =eval (input("请输入年份：\n"))
if leapyear(year)==1:
    print(year,"是闰年!")
else:
    print(year,"不是闰年!")