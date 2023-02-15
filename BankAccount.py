# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        #인스턴스 멤버 변수
        self.__id = id
        self.__name = name 
        self.__balance = balance
    #인스턴스 메서드  
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        return "{0}, {1}, {2}".format(self.__id, 
        self.__name, self.__balance)
    

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)

# 원래는 클래스가 나오는데 __Str__ 약속어로 문자열 리턴
print(account1)

# 잔고를 변경할수 있음 그래서 private 처리 ex) __ 처리 
account1.balance = 1500000

# 이름 규칙: _클래스명__변수명
print(account1._BankAccount__balance)



