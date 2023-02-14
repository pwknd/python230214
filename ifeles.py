#ifeles.py


score = int(input("점수를 입력:"))

if 90 <= score <= 100:
    grade = "a"

elif 80 <= score < 90:
    grade = "b"

elif 70 <= score <80:
    grade = "c"
else:
        grade = "d"

print("등급은", grade)

 

lst = ["11",100,3.14]
for item in lst:
    print(item)

    
colors = {"apple":"red","kiwi":"green"}
for k,v in colors.items():
    print(k,v)
    
