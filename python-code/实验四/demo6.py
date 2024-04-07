x=eval(input('Input a integer:'))
ls =[]
while x >0:
    ls.append(x%10)
    x//=10
print("整数位数：",len(ls))
print("逆序结果：",ls)