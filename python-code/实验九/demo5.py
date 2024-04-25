def sumall(re):
    account=0
    for i in re:
        account+=i
    return(account)
try:
    ls=[1,3,4,5]
    print(sumall(ls))
except:
    print("输入错误")