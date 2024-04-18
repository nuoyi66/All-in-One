import re
s="""693152032@**.com,werksdf@***.com,sdf@****.com
     sfjsdf@***.com,soifsdfj@***.com"""
content=re.sub(r"\w+@\w+.com","ahutcyz@***.com",s)
print(s)
print("____________________________")
print(content)