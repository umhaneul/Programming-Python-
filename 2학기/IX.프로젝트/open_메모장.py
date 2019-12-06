import pyautogui as pag
import time
if __name__ == '__main__' :
    #메모장 프로그램 실행하자
    pag.press("winleft")
    pag.typewrite("memo")
    time.sleep(1)
    pag.hotkey("enter")
    time.sleep(1)
    #hello world 하자
    pag.typewrite("hello world")
    time.sleep(1)
    #두 줄 내리자
    pag.press("enter",presses=2) #두번 연속
    time.sleep(1)
    #반갑구나 세상아 치자
    pag.press("hangul")
    pag.typewrite("qksrkqrnsk tptkddk")
    time.sleep(1)
    #helloworld 저장하자
    pag.hotkey("ctrl", "s") #pag.hotkey(["ctrl", "s"])
    time.sleep(1)
    pag.press("hangul")
    pag.typewrite("hello world")#pag.typewrite("C:\\Users\\user\\Desktop\\hello world") 원하는 경로를 앞에 써주기
    time.sleep(1)
    pag.hotkey("enter")

