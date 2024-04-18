s="""
340503199712120025
31002019900101003X
230102700205010
340503197601210020
"""
import re
regex=re.compile(r'(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)')
t=regex.finditer(s)
for i in t:
    print(s[i.start():i.end()])
