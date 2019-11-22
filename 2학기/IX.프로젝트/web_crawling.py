#터미널 > pip install bs4
#터미널 >pip install lxml

from bs4 import BeautifulSoup   #html 구조적으로 변환하자  alt+shift+enter
from urllib.request import urlopen #url에 해당하는 html 가져오자

if __name__=='__main__':
    # 네이버 웹툰 > 신의 탑 제목 가져오자
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=183559")
    print(data)
    soup = BeautifulSoup(data,"lxml")
    print(soup)

    cartoon_titles = soup.find_all("td",attrs = {'class':'title'})
    for title in cartoon_titles:
        t = title.find('a').text
        print(t)

    #다음 웹툰 > 어쩌다 발견한 7월
    # data = urlopen('http://webtoon.daum.net/webtoon/view/findjuly') #url -> httpRespones객체
    # soup = BeautifulSoup(data, "lxml")
    # cartoon_titles = soup.find_all("string",attrs={"class":"tit_wt"})
    # for title in cartoon_titles:
    #     print(title)



