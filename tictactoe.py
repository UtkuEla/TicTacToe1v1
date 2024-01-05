# Simple 1v1 TicTacToe game with OOP understanding.
import numpy as np
import os

class TicTacToe():

    def __init__(self) -> None:
        
        self.board = np.zeros((3,3))
        self.possible_moves = [0,1,2]
        self.gameplay()

    def firstPlayerMove(self) -> None:

        x, y = map(int, input("Coordinates for X: "))
        
        if x not in self.possible_moves or y not in self.possible_moves:
            print('Please choose appropriate coordinates.')
            self.firstPlayerMove()

        if self.board[x][y] == 0:
            self.board[x][y] = 1
            self.winCheck()
            self.showBoard()
        else:
            print('Please choose an appropriate place.')
            self.firstPlayerMove()

    def secondPlayerMove(self) -> None:

        x, y = map(int, input("Coordinates for O: "))

        if x not in self.possible_moves or y not in self.possible_moves:
            print('Please choose appropriate coordinates.')
            self.secondPlayerMove()

        if self.board[x][y] == 0:
            self.board[x][y] = 4
            self.winCheck()
            self.showBoard()
        else:
            print('Please choose an appropriate place.')
            self.secondPlayerMove()

    def showBoard(self) -> None:

        board_sub = self.board
        board_sub = np.where(board_sub == 1, 'X', board_sub)
        board_sub = np.where(board_sub == '4.0', 'O', board_sub)
        board_sub = np.where(board_sub == '0.0', ' ', board_sub)
        
        print("|---|---|---|")
        for i in range(3):
            for j in range(3):
                if j == 2:
                    print(f"| {board_sub[i, j]}",end=' | ')
                else:
                    print(f"| {board_sub[i, j]} ",end='')
            print("\n|---|---|---|")
    
    def winCheck(self) -> None:
        
        row_sums = np.sum(self.board, axis=1)
        column_sums = np.sum(self.board, axis=0)
        main_diagonal_sum = np.sum(np.diag(self.board))
        other_diagonal_sum = np.sum(np.diag(np.fliplr(self.board)))

        if np.any(row_sums == 3) or np.any(column_sums == 3) or main_diagonal_sum == 3 or other_diagonal_sum == 3:
            print('Player 1 won!')
            self.showBoard()
            exit()

        elif np.any(row_sums == 12) or np.any(column_sums == 12) or main_diagonal_sum == 12 or other_diagonal_sum == 12:
            print('Player 2 won!')
            self.showBoard()
            exit()

        # if any(val == 3 for val in (np.any(row_sums == 3), np.any(column_sums == 3), main_diagonal_sum == 3, other_diagonal_sum == 3)):
        #     print('Player 1 won!')
        # elif any(val == 12 for val in (np.any(row_sums == 12), np.any(column_sums == 12), main_diagonal_sum == 12, other_diagonal_sum == 12)):
        #     print('Player 2 won!')

    def gameplay(self) -> None:
        print("Welcome to the TicTacToe Game!\n")
        self.showBoard()

        while True:

            if 0 not in self.board:
                print('Game is draw!')
                exit()

            self.firstPlayerMove()
            os.system('cls')
            self.showBoard()
            
            if 0 not in self.board:
                print('Game is draw!')
                exit()           

            self.secondPlayerMove()
            os.system('cls')
            self.showBoard() 

if __name__ == "__main__":
    game = TicTacToe()