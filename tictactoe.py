# Simple 1v1 TicTacToe game with OOP understanding.
import numpy as np
import os

class TicTacToe():

    def __init__(self) -> None:
        
        self.board = np.zeros((3,3))
        self.possible_moves = [0,1,2] 
        self.gameplay()

    def makeMove(self, counter: int) -> None:
        print(counter)
        
        if counter%2 == 1:
            x, y = map(int, input("Coordinates for X: "))

            while x not in self.possible_moves or y not in self.possible_moves:
                print('Please choose appropriate coordinates.')
                x, y = map(int, input("Coordinates for X: "))
    
            print(x,y)
            if self.board[x][y] == 0:
                self.board[x][y] = 1
                self.showBoard()
            else:
                print('Please choose an appropriate place.')
                self.makeMove(counter)

        else:
            x, y = map(int, input("Coordinates for O: "))

            if x not in self.possible_moves or y not in self.possible_moves:
                print('Please choose appropriate coordinates.')
                x, y = map(int, input("Coordinates for O: "))
            
            if self.board[x][y] == 0:
                self.board[x][y] = 4
            else:
                print('Please choose an appropriate place.')
                self.makeMove(counter)

    def showBoard(self) -> None:

        board_sub = self.board
        board_sub = np.where(board_sub == 1, 'X', board_sub)
        board_sub = np.where(board_sub == '4.0', 'O', board_sub)
        board_sub = np.where(board_sub == '0.0', ' ', board_sub)
        
        os.system('cls')
        print("|---|---|---|")
        for i in range(3):
            for j in range(3):
                if j == 2:
                    print(f"| {board_sub[i, j]}",end=' | ')
                else:
                    print(f"| {board_sub[i, j]} ",end='')
            print("\n|---|---|---|")
    
    def winCheck(self) -> int:
        
        row_sums = np.sum(self.board, axis=1)
        column_sums = np.sum(self.board, axis=0)
        main_diagonal_sum = np.sum(np.diag(self.board))
        other_diagonal_sum = np.sum(np.diag(np.fliplr(self.board)))

        if np.any(row_sums == 3) or np.any(column_sums == 3) or main_diagonal_sum == 3 or other_diagonal_sum == 3:
            return 1

        elif np.any(row_sums == 12) or np.any(column_sums == 12) or main_diagonal_sum == 12 or other_diagonal_sum == 12:
            return 2

        return 0
    
    def gameplay(self) -> None:
        print("Welcome to the TicTacToe Game!\n")
        self.showBoard()

        counter = 1
        while True:

            if 0 not in self.board:
                self.showBoard()
                print('Game is draw!')
                break

            self.makeMove(counter)
            
            if self.winCheck() == 1:
                self.showBoard()
                print("Player 1 won!")
                break

            elif self.winCheck() == 2:
                
                self.showBoard()
                print("Player 2 won!")
                break

            counter = counter +1

            
            self.showBoard()
        
        print("\nThank you for playing!\n")
        exit()

if __name__ == "__main__":
    game = TicTacToe()