item=[11,22,33,44,55,66,77,88,99]
item1=[]
item2=[]
items={'k1':'','k2':''}
for i in item:
    if i<=66:
        item1.append(i)
    else:
        item2.append(i)
items['k1']=item1
items['k2']=item2
print(items)