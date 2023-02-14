# function3.py
# 기본값 세팅
def times(a=10, b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드인자 방식
def connectURI(server, port):
    starURL = "https://" + server + ":" + port
    return starURL

#호출
print(connectURI("credu.com","80"))
print(connectURI(port="8080", server="credu.com"))


#가변인자(가변적인 상황처리)
def union(*ar):
    result = []
    for items in ar:
        for x in items:
            if x not in result:
                result.append(x)
    return result

#호출
print( union("ham","egg"))
print( union("ham","egg","spam"))


#정의되지 않은 인자 처리
def userURILBuilder(server, port, **user):
    starURL = "https://" + server + ":" + port + "/?"
    for key in user.keys():
        starURL += key + "=" + user[key] + "&"
    return starURL

#호출 
print( userURILBuilder("credu.com","80", id="kim", passwd="1234"))
print( userURILBuilder("credu.com","80", id="kim", passwd="1234", name="mike"))



#람다함수(함수를 정의하는 간단한 문법)
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3))
print( globals())
