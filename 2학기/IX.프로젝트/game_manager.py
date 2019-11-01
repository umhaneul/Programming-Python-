from tictactoe import TicTacToe
import tkinter

class Gamemanager:
    def __init__(self):
        self.ttt = TicTacToe()

    def play(self):
        #show_bord

        #반복하자
        while True:
            #위치를 입력 받자
            row = int(input("row: "))
            col = int(input("col: "))
            #말을 놓자
            self.ttt.set(row,col)
            print(self.ttt)
            #check_winner()
            if self.ttt.check_winner() == "o":
                print("O 승리,ㅊㅋㅊㅋ")
                break
            elif self.ttt.check_winner() == "x":
                print("x 승리,ㅊㅋㅊㅋ")
                break
            elif self.ttt.check_wiiner() == "d":
                print("무승부")
                break
        #결과 출력하자

class GameManager_GUI:
    def __init__(self):
        self.ttt = TicTacToe()
        CANVAS_SIZE = 300
        self.TILE_SIZE = CANVAS_SIZE/3

        self.root = tkinter.Tk()#창 frame
        self.root.title("틱 택 토")
        self.root.geometry(str(CANVAS_SIZE)+"x"+str(CANVAS_SIZE)) #geometry("300x300")
        self.root.resizable(width=False, height=False)
        self.canvas = tkinter.Canvas(self.root, bg="white", width=CANVAS_SIZE, height=CANVAS_SIZE)

        self.canvas.pack()

        self.images = dict()
        self.images["o"] = tkinter.PhotoImage(file="img/o.gif")
        self.images["x"] = tkinter.PhotoImage(file="img/x.gif")
        self.canvas.bind("<Button-1>",self.chick_handler)
    def click_handler(self, event):
        row = math.floor(event.y/self.TILE_SIZE)
        col = math.floor(event.x/self.TILE_SIZE)
        self.ttt.set(row,col)
        self.draw_board()
        #check_winner()

    def draw_board(self):
        #closer
        self.canvas.delete("all")

        SIZE = 100
        x = 0
        y = 0
        for i,v in enumerate(self.ttt.board):
            if v == ".":
                pass
            elif v == "o":
                self.canvas.create_image(x,y, anchor="nw", image=self.images["o"])
            elif v == "x":
                self.canvas.create_image(x,y, anchor="nw", image=self.images["x"])
            x += self.TILE_SIZE
            if i % 3 == 2:
                x = 0
                y += self.TILE_SIZE

    def play(self):
        self.root.mainloop()

if __name__ == '__main__':
     gm = GameManager_GUI()
     gm.play()
     gm.ttt.set(1,1)
     gm.draw_board()
     gm.draw_board()
