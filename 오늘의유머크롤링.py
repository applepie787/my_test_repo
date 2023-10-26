# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

f = open("c:\\work\\today.txt", "wt", encoding="utf-8")
for n in range(1,30):
        #클리앙의 중고장터 주소 
        #data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        data = "https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=" + str(n)
        print(data)

        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})
        #<td class="subject">
        # <a href="/board/view.php?table=bestofbest&amp;no=471497&amp;s_no=471497&amp;page=1" target="_top">우리나라 지금 현재 전쟁나면 필패인 이유 추가</a><span class="list_memo_count_span"> [18]</span>   </td>
        # <span class="subject_fixed" data-role="list-title-text" title="아이폰 13프로 256 블루 (북미판) 새로 리퍼 받은 S급">
	# 					아이폰 13프로 256 블루 (북미판) 새로 리퍼 받은 S급
	# </span>

        for item in list:
                #에러처리(try ~ catch)
                try:
                        title = item.find("a").text.strip()
                        if re.search("일본",title):
                            print(title)
                            f.write(f"{title}\n")

                        # if (re.search('아이폰', title)):
                        #         print(title.strip())
                        #         print('https://www.clien.net'  + item['href'])
                except:
                        pass
        
f.close