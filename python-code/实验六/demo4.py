d={1:'a',2:'b',3:'c',4:'d'}
v=eval(input("请输入一个键：\n"))
if v in d:
    print(d[v])
else:
    print("您输入的键不存在")