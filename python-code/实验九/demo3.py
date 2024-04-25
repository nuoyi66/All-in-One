def mysqrt(a,e):
    if a<0:
        a=-a
    if a==0:
        return 0
    x1=1.0
    while True:
        x2=(x1+a/x1)/2
        if abs(x2-x1)>e:
            x1=x2
        else:
            break
    return x2
a=3
e=1e-5
print(a,"的平方根=",mysqrt(a,e))