#class1.py
# 1)클래스 정의
class Person:
    #초기화 메서드
    num_person = 0 
    def __init__(self):
        self.name = "defailt name"
        Person.num_person += 1 
    def print(self):
        print("My name is {0}".format(self.name))

#2) 인스턴스 생성
p1 = Person()
p2 = Person()
p2 = Person()
print("인스턴스 갯수:{0}".format(Person.num_person))

Person.age = 30 
print(p1.age)
print(p2.age)