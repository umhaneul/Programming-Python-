#유튜브 레드벨벳 1주 업로드 영상
from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__ == '__main__' :
    with urlopen("https://www.youtube.com/results?search_query=%EB%A0%88%EB%93%9C%EB%B2%A8%EB%B2%B3&sp=EgIIAw%253D%253D") as response :
        soup = BeautifulSoup(response, "lxml")
    # print(soup)

    video_titles = soup.find_all("a", attrs={"class": "yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link"})
    print("유튜브 레드벨벳 1주 업로드 영상")

    for video_title in video_titles[:]:
        link = video_title.get("href")
        link = "https://www.youtube.com/" + link
        print(video_title.text)
        print(link)
        # link = video_title.find("a").get("href")
        # link = "https://www.youtube.com/" + link
        # print(t)
        # print(link)