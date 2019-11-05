from tkinter import *
from school import School

class Local():
    #root = Tk()
    root = Tk()
    root.geometry('800x500')
    root.configure(bg='#87CEEB')
    root.title("고교탐험")

    local1 = PhotoImage(file='imgs/l1.png')
    local2 = PhotoImage(file='imgs/l2.png')
    local3 = PhotoImage(file='imgs/l3.png')
    local4 = PhotoImage(file='imgs/l4.png')
    local5 = PhotoImage(file='imgs/l5.png')

    btn1 = Button(root,image=local1)
    btn2= Button(root,image=local2)
    btn3= Button(root,image=local3)
    btn4= Button(root,image=local4)
    btn5= Button(root,image=local5)
    btn1.place(x=200, y=200)
    btn2.place(x=400,y=201)
    btn3.place(x=500,y=100)
    btn4.place(x=600,y=100)
    btn5.place(x=700,y=100)

    root.mainloop()

