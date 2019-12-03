from bs4 import BeautifulSoup
#from urllib.request import urlopen
import requests

if __name__ == '__main__' :
    url ="https://www.youtube.com/feed/trending"
    #url ="https://www.youtube.com/user/feellikefeel"
    response = requests.post(url)   #post방식으로 request
    soup = BeautifulSoup(response.text, "lxml")
    #print(soup)
    youtube_titles = soup.find_all("a",attrs={"class":"yt-uix-tile-link"})  #주로 a태그, 주고 class로 찾으면 쉬움
    for youtube_title in youtube_titles:
        print(youtube_title.text)
        print("https://www.youtube.com/" + youtube_title["href"])   #youtube_title.get("href") 속성값가져오는 방법
