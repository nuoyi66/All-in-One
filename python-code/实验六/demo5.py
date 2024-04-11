import random

li1 = []
d = dict()

for i in range(1000):
    li1.append(random.randint(20, 100))

for i in li1:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

li2 = list(set(li1))
li2 = sorted(li2)
print(li2)
print(d)