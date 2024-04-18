import re
s="""se234 1987-02-09 07:30:00
     1987-02-10 07:25:00"""
content=re.findall(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",s,re.M)
print(s)
print(content)