a=10
b=20
if (a and b):
  print("1-变量a和b都为true")
else:
  print("1-变量a和b有一个不为true")
if( a or b):
  print("2 - 变量a和b都为true，或其中一个变量为true")
else:
  print("2-变量a和b都不为true")
a=0
if(a and b):
  print("3-变量a和b都为true")
else:
  print("3-变量a和b有一个不为true")
if(a or b):
  print("4一变量a和b都为true，或其中一个变量为true")
else:
  print("4-变量a和b都不为true")
if not(a and b):
  print("5-变量a和b都为false，或其中一个变量为false")
else:
  print("5一变量a和b都为true")