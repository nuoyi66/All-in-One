import random
x=[random.randint(0,100)for i in range(20)]
print(x)
y=x[::2]
y.sort(reverse=True)
x[::2]=y
print(x)