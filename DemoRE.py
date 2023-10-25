#DemoRE.py

import re
result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

result = re.search("apple", "this is Apple".lower())
print(result.group())

result = re.search("\d{4}", "올해는 2323년 입니다.")
print(result.group())

result = re.search("\d{5}", "우리 동네는 52524")
print(result.group())


#컴파일 함수를 사용
data = "Apple is big company and apple is delicious"
c = re.compile("apple", re.IGNORECASE)
print(c.findall(data))

data = """다중 라인으로
만든 문자열

데이터"""

c = re.compile("^.+", re.MULTILINE)
print(c.findall(data))