#DemoRE.py

import re

#포함하는 경우(처음부터 끝까지 검색)
result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

#정확하게 일치하는 경우(첫번째만 검색)
result = re.match("[0-9]*th", "35th")
print(result)
print(result.group())

result = re.search("ap", "this is apple")
print(result.group())
result = re.search("\d{4}", "올해는 2023년")
print(result.group())


#다중 라인 포함 
s ="""Gee Gee Gee 

너무 부끄러워 

쳐다볼 수 없어
"""

c= re.compile("^.+", re.MULTILINE)
print(c.findall(s))