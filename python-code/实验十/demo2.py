f = open("temp.txt",'r')
ht = f.readline().strip()
L1 = list(ht.split(' '))
lt = f.readline().strip()
L2 = list(lt.split(' '))
f.close()
L3 = []
sum = 0
for i in range(len(L1)):
    L1[i] = int(L1[i])
    L2[i] = int(L2[i])
    L3.append((L1[i] + L2[i]) / 2)
    sum += L3[i]
print(L1)
print(L2)
print("一周最高气温:", max(L1))
print("一周最低气温:", min(L2))
print("一周平均气温: {%.2f}" % (sum / len(L3)))