a=[1,4,6,9,13,16,19,28,40,100,0]
print('原始列表:')
for i in range(len(a)):
    print(a[i],end=' ')
number = int(input('\n请输入一个整数:'))
end=a[9]
if number>end:
    a[10]=number
else:
    for i in range(len(a)):
        if number<a[i]:
            temp1=a[i]
            a[i]=number
            for j in range(i+1,len(a)):
                temp2=a[j]
                a[j]=temp1
                temp1=temp2
            break
print('排序后的列表:')
for i in range(len(a)):
    print(a[i],end=' ')