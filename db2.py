#db1.py

import sqlite3

#연결객체(파일에 저잘)
con = sqlite3.connect("c:\\work\\sample.db")
#커서객체
cur = con.cursor()
#테이블 구조 생성
cur.execute("""create table if not exists PhoneBook
(id integer primary key autoincrement, name text, phoneNum text);
""")

#1건 입력
name = "홍길동"
phoneNumber = "010-3454"
cur.execute("insert into PhoneBook (name, phoneNum) values (?,?);",
            (name, phoneNumber))
#다중으로 행을 입력
datalist = (("박문수", "010-333"), ("김길동", "010-567"), ("김길동", "010-45456"))
cur.executemany("insert into PhoneBook (name, phoneNum) values (?, ?);", datalist)

#검색
cur.execute("select * from PhoneBook;")
print(cur.fetchall())

#작업 완료
con.commit()

