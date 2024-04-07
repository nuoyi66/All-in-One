import random
x=[random.randint(0,100)for i in range(50)]
print(x)
i=len(x)-1
while i>=0:
    if x[i]%2==1:
        del x[i]
    i-=1
print(x)