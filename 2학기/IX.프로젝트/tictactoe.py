class TicTacToe:
    def __init__(self):
        self.board = [".",".",".",".",".",".",".",".","."]
        self.current_turn = "O"

    def set(self, row, col):
        if self.get(row, col) == ".": #빈칸일 경우에만 말을 놓을 수 있도록하지
         self.board[(row * 3) + col] = self.current_turn
        # if self.current_turn == "O" :
        #     self.current_turn == "X"
        # else :
        #     self.current_turn = "O"
        self.current_turn = "X" if self.current_turn == "O" else "O"
        self.board

    def get(self, row, col):
        self.board[(row * 3) + col]

    def check_winner(self):
        check = self.current_turn
        #가로 -
        for i in range(3):
            if self.get(i,0) == self.get(i,1) == self.get(i,2) == check:
                return check
        #수직
            if self.get(0,i) == self.get(1,i) == self.get(2,i) ==  check:
                return check

        if self.get(0,0) == self.get(1,1) ==  self.get(2,2) == check :
            return check
        if self.get(0,0,) == self.get(1.0) == self.get ==(2,0) == check:

        #무승부 if"." islef.board:
            return "d"

    def __str__(self):
        s = ""
        for i,ch in enumerate(self.board):
            s += ch
            if i%3 == 2:
                s +="\n"
        return s

if __name__ == '__main__':
    ttt = TicTacToe()
    print(ttt)
    ttt.set(0, 0)
    ttt.set(0, 1)
    ttt.set(1, 0)
    ttt.set(1, 1)
    ttt.set(2, 0)
    ttt.set(2, 2)
    print(ttt)