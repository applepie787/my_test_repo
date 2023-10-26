# Web1.py

#웹크롤링
from bs4 import BeautifulSoup

#페이지 로딩
page = open("c:\\work\\test01.html", "r", encoding="utf-8").read()
#검색이 용이한 객체 생성
soup = BeautifulSoup(page,"html.parser")
#전체 보기
#print(soup.prettify())

#<p>태크 전체를 검색
#print(soup.find_all("p"))

#첫번째 <p>만 검색
#print(soup.find("p"))
#<p class="outer-text">형태만 검색
#print(soup.find_all("p", class_="outer-text"))
# attrs를 사용(Attributes)
#print(soup.find_all("p", attrs={"class":"outer-text"}))

#특정 채그만 지정할 경우 id속성
#print(soup.find_all(id="first"))

#태크 내부의 컨텐츠를 가져오기: .text
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n","")
    print(title)


    