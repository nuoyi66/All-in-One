import re
s1='adkkdk'
s2='abc123efg'
an=re.search('^[a-z]+$',s1)
if an:
    print('s1:',an.group(),'全为小写')
else:
    print(s1,"不全为小写!")
an=re.match('[a-z]+$',s2)
if an:
    print('s2:',an.group(),'全为小写')
else:
    print(s2,"不全为小写!")