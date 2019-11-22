#2412 엄하늘
#비밀번호를 입력하여 비밀번호가 일치하면 메모장을 실행 할 수 있는 프로그램(불러오기, 저장하기 가능)
from tkinter import * #창을 보여주기 위해 모듈선언

class User(Frame):
    def __init__(self,root):#변수 self, root 선언
        Frame.__init__(self,root)
        self.root = root
        self.pack(expand=YES, fill=BOTH)
        self.createWidgets()
        self.onNew()
        self.fileName = "문서.txt"

    def createWidgets(self):#파일에 들어가는 메뉴 추가해주기
        self.menubar=Menu(self)

        self.master.config(menu=self.menubar)

        file = Menu(self.menubar)
        file.add_command(label='새로 만들기', command=self.onNew)
        file.add_command(label='열기', command=self.onOpen)
        file.add_command(label='저장', command=self.onSave)
        # file.add_separator()
        file.add_command(label='끝내기', command=self.onExit)
        self.menubar.add_cascade(label='파일', menu=file)

        self.text=tbox=Text(self, relief=SUNKEN)
        sbar=Scrollbar(self)#스크롤바 생성
        sbar.config(command=tbox.yview)#스크롤바가 움직일때 실행 메서드
        tbox.config(yscrollcommand=sbar.set)#스클롤바 적용
        sbar.pack(side=RIGHT, fill=Y)#오른쪽으로 이동
        tbox.pack(side=LEFT, expand=YES, fill=BOTH)
        tbox.focus()

    def onNew(self):#새로만들기 함수
        self.file=None
        self.text.delete('1.0', END)
        self.master.title('메모장')

    def onOpen(self):#열기 함수
        f = open(self.fileName, mode='rt', encoding='utf-8')
        op = f.read()
        self.text.delete(1.0,END)
        self.text.insert(END,op)

    def onSave(self):#저장 함수
        f = open(self.fileName, mode='wt',encoding="utf-8")
        f.write(self.text.get('1.0',END))
        f.close()

    def onExit(self):#닫기 함수
        self.root.destroy()
        self.root.quit()

if __name__ == '__main__' : 
    # in_str = input("비밀번호를 입력해 주세요:\n")
    #
    # a_str = input("다시 한번 입력해 주세요: ")
    #
    # if in_str==a_str:
    #     b = str(input("메모장을 실행하시겠습니까?(y/n):"))
    #     if 'y' or 'Y' :
            root = Tk()#Tk클래스 객체(root)생성
            User(root).mainloop()# mainloop()메서도 호출
    #     elif 'n' or 'N' :
    #         pass
    #
    # else:
    #     s = input("다시 입력해 주세요 : ")
    #     if s==in_str:
    #         root = Tk()
    #         #UserMyEdit(root).mainloop()
