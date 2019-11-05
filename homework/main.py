from tkinter import *
from local import Local

class start() :
    root = Tk()
    root.geometry('800x500')
    root.configure(bg='#87CEEB')
    root.title("고교탐험")

    photo2 = PhotoImage(file='imgs/i2.PNG')
    btn = Button(root,image=photo2,command=root.Local)

    btn.place(x=280, y=120)
    root.mainloop()

