#demoSetTuple.py

tp = (1,2,3)
print(len(tp))
print(tp[0])

#함수를 정의
def  calc(a,b):
    return a+b, a*b

#함수를 호출
result = calc(3,4)
print(result)

# set 연습 
print("---set 연습---")

a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a|b)
print(a&b)
print(a-b)
