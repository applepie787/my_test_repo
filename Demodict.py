# Demodict.py

phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print(phone)
print(len(phone))
print(phone["kim"])
print("kim" in phone)
print("kang" not in phone)


P = phone

P["kang"] = "1234"
print(P)
print(phone)
print(id(phone), id(P))


#장비 관리
device = {'아이폰':5, '아이패트':10}

device["맥북"] = 15
device["아이폰"] = 6

print(device)
del device["아이폰"]
print(device)

for item in device.items():
    print(item)
for item in device.keys():
    print(item)
for item in device.values():
    print(item)

print(bool(0))
print(bool(3))
print(bool(""))
print(bool("test"))
print(bool([]))
print(bool([1,2,3]))

print(5/2)
print(5//2)
print(5%2)
