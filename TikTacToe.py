"""
Structure

Start Game (if p1 went first last time p2 gets to start this time)
P1 (X's)
P2 (O's)

Track all boxes, 3 lists
1 2 3
4 5 6
7 8 9


concatenate into one list and check winning scenarios


reset game or quit
"""
import Board
import Player

class TikTacToe:
    def __init__(self):
        board = Board.Board()
        board.begin_game()
        pass


start = TikTacToe()

