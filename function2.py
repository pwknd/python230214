# function2.py
print("----불변-----")

a = 1.2 
print(id(a))

a= 2.3
print(id(a))



print("------가변형식------")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

# 전역변수 
x= 5 

def func(a):
    return a+x 

#호출 

print(func(1))


#지역변수 
def func2(a):
    x = 1
    return a+x 

#호출 
print(func2(1))



# 디버깅 연습용 교집한 리턴 함수 
def intersect(prelist,postlist):
    #지역변수에 교집합 문자 모으기 
    result = [] 
    for x in prelist:
        # x에 ham 중 a가 있고 result에 없으면 a를 추가해라 
        if x in postlist and x not in result: 
            result.append(x)
    return result
# 호출 
print(intersect("Ham","Spam"))



#전역변수(불변)에 읽기+쓰기
g=1
def testScope(a):
    #global g 
    g = 2
    return a+g
#호출
print(testScope(1))
print("전역변수 g:",g)

#가변형식
wordlist = ["J","A","M"]
def change(x):
    #    x[0] = "h"
    # 복사본 생성
    x1 = x[:]
    x1[0] = "H"

    print("함수 내부:", x1)

#호출(pass by reference, Call by reference)
change(wordlist)
print(wordlist)

