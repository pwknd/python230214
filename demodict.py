#demodict

print("-------형식변환-------")

b = set((1,2,3))
print(type(b))
print(b)
c = list(b)
c.append(4)
print(c)

print("-------딕셔너리-------")

color = {"apple":"red", "banana":"yellow"}
print(len(color))
print(color["banana"])
color["cherry"]="red"
print(color)
del color["apple"]
print(color)


GG = list(color)
print("ＧＧ출력",GG)

print("-------딕셔너리 키값-------")
device = {"아이폰":5, "banana":2, "리스트":6}
print(device)

II = list(device)
print("II출력",II)
HH = set(device)
print("HH출력",HH)


print ("----명함관리----")
phone = {"kim":"1111", "lee":"2222","park":"33333"}
print("kim" in phone)
print("moon" in phone)

for item in phone.items():
    print(item)

for k,v in phone.items():
    print(k,v)


print ("----call by ref----")
p = phone
phone["moon"] = "1234"
print(phone)
print(p)
print(id(phone), id(p))

a = {"kim":"1","park":"2","back":"3"}
b = a
a[0] = 38 
print(a)
print(b)
print(id(a), id(b))

print("------- deep copy-------")

import copy

b = copy.deepcopy(a)
print(id(a),id(b))


isRight = True
print(type(isRight))
print(1 < 2)
print(1 == 2)
print(1 != 2)
print( True and True and True)
print( True and True and False)
print( True or False or False)