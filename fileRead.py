#fileRead.py

import re

f = open("d:/work/demo.txt","rt", encoding="utf-8")

names = f.readlines()




print(names)

for name in names:
    c= re.sub("\n","",name)    
    print("안녕하세요 {0}님 봄입니다.".format(name))
    print("="* 40)