import re
s="""i love you not because of who 234 you are,234 but 3234ser because of who i am when i am with you"""
content=re.findall(r"\b[a-zA-Z]+b",s)
print(content)