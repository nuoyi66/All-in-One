def output(s,l):
    if l==0:
        return
    print (s[l-1],end='')
    output(s,l-1)
s=input('Input a string:\n')
n=len(s)
output(s,n)