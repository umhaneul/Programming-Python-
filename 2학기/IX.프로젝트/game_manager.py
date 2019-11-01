from tictactoe import TicTacToe
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

if __name__ == '__main__':
     gm = Gamemanager()
     gm.play()