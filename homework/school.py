from tkinter import *

class School():
    root = Tk()
    root.geometry('800x500')
    root.configure(bg='#87CEEB')
    root.title("고교탐험")

    shcool1 = PhotoImage(file='imgs/school.png')
    #local2 = PhotoImage(file='imgs/l2.png')

    btn1 = Button(root,image=shcool1)
    #btn2= Button(root,image=local2)
    btn1.place(x=300, y=200)

    root.mainloop()

