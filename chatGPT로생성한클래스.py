# Person 클래스 정의
class Person:
    def __init__(self, id, phoneNumber):
        self.id = id  # ID 변수
        self.phoneNumber = phoneNumber  # 전화번호 변수
    
    def printinfo(self):
        print(f"ID: {self.id}, 전화번호: {self.phoneNumber}")

# Manager 클래스, Person 클래스를 상속
class Manager(Person):
    def __init__(self, id, phoneNumber, title):
        super().__init__(id, phoneNumber)  # 부모 클래스의 생성자 호출
        self.title = title  # 직책 변수
    
    def printinfo(self):
        super().printinfo()  # 부모 클래스의 printinfo 메서드 호출
        print(f"직책: {self.title}")

# Employee 클래스, Person 클래스를 상속
class Employee(Person):
    def __init__(self, id, phoneNumber, title):
        super().__init__(id, phoneNumber)  # 부모 클래스의 생성자 호출
        self.title = title  # 직책 변수

    def printinfo(self):
        super().printinfo()  # 부모 클래스의 printinfo 메서드 호출
        print(f"직책: {self.title}")

# 클래스 인스턴스 생성 및 사용 예시
person1 = Person("12345", "555-555-5555")
person1.printinfo()

manager1 = Manager("67890", "999-999-9999", "매니저")
manager1.printinfo()

employee1 = Employee("54321", "777-777-7777", "직원")
employee1.printinfo()
