#터미널 > pip install bs4 -> File > Settings... > Project... > Project interpreter > + > beautifulsoup4 > Install Package
#터미널 >pip install lxml -> File > Settings... > Project... > Project interpreter > + > lxml > Install Package
#pip install lxml

from bs4 import BeautifulSoup   #html 구조적으로 변환하자  alt+shift+enter
from urllib.request import urlopen #url에 해당하는 html 가져오자

if __name__ == '__main__':
    #urlopen 하자
    response = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=700844")
    soup = BeautifulSoup(response, "lxml")
    #print(soup)
    cartoon_titles = soup.find_all("td",attrs={"class":"title"})
    for title in cartoon_titles:
        t = title.find("a").text
        link = title.find("a").get("href")
        link = "https://comic.naver.com" + link
        print(t)
        print(link)
    #BeautifulSoup 객체 생성하자
    #원하는 태그나 속송으로 찾자
    #정보를 찾자
