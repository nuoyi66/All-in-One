h=0
leap=1
from math import sqrt
for m in range(101,201):
    k=int(sqrt(m+1))
    for i in range(2,k+1):
        if m%i == 0:
            leap =0
            break
    if leap == 1:
        print('%-4d'%m)
        h+=1
    leap = 1
print('The total is %d'%h)