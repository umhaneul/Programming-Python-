import pyautogui as pag
import time

if __name__ == '__main__' :
    #data = pag.locateOnScreen("크롬.PNG")
    #print(data)
    #pag.moveTo(data.left+(data.width/2), data.top+(data.heigth/2), duration=2)
    #center = pag.center(data)
    #print(center)
    center = pag.locateCenterOnScreen("크롬.png")
    pag.moveTo(center, duration=2)
    pag.doubleClick()