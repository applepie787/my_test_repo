# func2.py
# 스코핑룰(LGB규칙)

x = 1
def func1(a):
    return a+x


print(func1(1))

def func2(a):
    x=5
    return x+a

print(func2(1))

# 기본값이 있는 경우

def times(a=10, b=20):
    return a+b

print(times())
print(times(3))
print(times(5, 6))

# 키워드인자방식(매개변수명을 기술하는 경우)
def connectURL(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

#호출
print(connectURL("multi.com", "80"))
print(connectURL(port="8080", server="multi.com"))

#가변인자:가변적인 상황(* Tuple의 경우)
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)

    return result

print(union("HAM", "SPAM"))
print(union("HAM", "SPAM", "EGG"))
print("------------------------------------------------------")

#람다(한줄로 기술하는 즉흥적인, 일회성 함수)
g = lambda x,y:x*y
print(g(3, 5))
print( (lambda x:x*x)(3))
print( globals() )
