#PyAutoGUI 설치하자
#pip install pyautogui
import time
import pyautogui as pag

if __name__ == '__main__' :
    # while True:
    #     x, y = pag.position()
    #     print("x : {} \ty: {}".format(x,y), end="\r")   #r=내리지 않고 맨 앞으로
    # pag.moveTo(230,374, duration=2)  #~어디 이동
    # pag.move(100,200, duration=2)     #~만큼 이동
    # pag.click()
    # pag.click()
    # pag.doubleClick() #더블클릭
    # pag.click(clicks=2)
    # pag.drag(0, 200, duration=1)  #드래그 duration있어야 함
    # pag.rightClick()  #오른쪽 버튼
    # pag.click(230,374, duration=2)
    #pag.doubleClick(230,374,duration=2)
    # time.sleep(1)   #크롬이 열리기를 기다려야 함
    # pag.typewrite("http://ticket.interpark.com/")
    # pag.press("enter")
    # # pag.press("hangul")   #한/영키
    # # pag.typewrite("아이유")  #아이유 영어로
    # pag.press("enter")
    # TODO: pag.scroll
    pag.hotkey("alt","tab") #단축키
    time.sleep(2)
    # pag.scroll(clicks=-2000, x=1018, y=304)
    pag.scroll(-2000, x=1018, y=304)