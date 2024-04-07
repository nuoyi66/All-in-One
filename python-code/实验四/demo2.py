import math
n=0
count=0
while True:
    first=n+100
    second=n+168
    first_sqrt=int(math.sqrt(first))
    second_sqrt=int(math.sqrt(second))
    if(first_sqrt*first_sqrt==first)and(second_sqrt*second_sqrt==second):
        print(n)
        break
    n+=1