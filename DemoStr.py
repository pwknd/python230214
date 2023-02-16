#DemoStr.py
s = "abcdef"
print(s[:2])
print(s[-2:])
print(len(s))

#특수문자(탈출문자)
print("c:\work\test.txt")
print("c:\\work\\test.txt")

#raw string notation(가공하지 않은 문자열)
print(r"d:\\work\\test.txt")

f = open("d:/work/demo.txt","rt", encoding="utf-8")

names = f.readlines()

print(names)

for name in names:
    print("안녕하세요 {0}님 봄입니다.".format(name),end="")
    print("="* 40)


print("---------------------------------------")

f = open("d:/work/demo.txt","wt", encoding="utf-8")

names =["김길동","홍길동","전우치"]

for name in names:
    f.write("안녕하세요 {0}님 봄입니다.".format(name))
    f.write("="* 40)
    f.write("\n")

#str 클래스의 메서드
#print(dir(str)) 

strA = "python is very powerful"
strB = "파이썬은 강력해"
print(strA.capitalize())
print(strA.upper())
print(len(strA))
print(len(strB))
print("----- 알파벳과 숫자로만 구성 ------")
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isalnum())
    
    
# 문자열을 가공(전처리)
# <<를 빼는 코드 
u= "<<spam and ham>>"
result = u.strip()
print(u)
print(result)




