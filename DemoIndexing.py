# demoIndexing.py

x = 100
y = 3.14

print(type(x))
print(type(y))

strA = "Python is very powerful"
strB = "파이썬은 강력해"

print(len(strA))
print(len(strB))

lst = [1,2,3]

for item in lst :
    print(item)

print("Index slicing --------")
print("strA[0] is : " + strA[0])
print("strA[1] is : " + strA[1])
print("strA[0:6] is : " + strA[0:6])
print("strA[:6] is : " + strA[:6])
print("strA[-3:] is : " + strA[-3:])
print("strA[-8:] is : " + strA[-8:])
print("strA[:] is : " + strA[:])

strC = """이 문자열을
다중 라인으로
저장합니다.
"""

print("이 문자열은 \t를 출력합니다.")
print(strC)

colors = ["red", "blue", "green"]
print(type(colors))
print(colors)
colors.append("yellow")
print(colors)