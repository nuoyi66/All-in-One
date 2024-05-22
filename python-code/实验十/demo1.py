f = open("1.txt","r")
s = f.readlines()
f.close()
r = [i.swapcase() for i in s]
f = open("2.txt","w")
f.writelines(r)
f.close()