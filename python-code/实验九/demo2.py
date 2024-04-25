def sigma(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    return (s)
n=eval(input("please input a number:\n"))
print(sigma(n))