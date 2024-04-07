a=20
b=20
if (a is b):
 print("1-a 和b有相同的标识")
else:
 print("1-a 和b没有相同的标识")
if(id(a) == id(b)):
 print("2-a和b有相同的标识")
else:
 print("2-a和b没有相同的标识")
b=30
if(a is b):
 print("3-a和b有相同的标识")
else:
 print("3-a和b没有相同的标识")
if(a is not b):
 print("4-a和b没有相同的标识")
else:
 print("4-a和b有相同的标识")