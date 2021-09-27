import Player


class Board:
    squares = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player_up_next = 'p1'

    def __init__(self):
        print('Each square is numbered 1-9 so for example the middle square is number 5')
        self.players = Player.player()
        pass

    def begin_game(self):
        # TODO give brief intro before the game start
        print('__________New Game__________')
        print('Player 1: ' + self.players.get_score('p1') + ' wins')
        print('Player 2: ' + self.players.get_score('p2') + ' wins')
        print('Ties: ' + str(self.players.ties))
        self.squares = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.draw_board()
        self.player_turn(self.player_up_next)
        pass


    def draw_board(self):
        separator = '+---+---+---+'
        print(separator)
        print('| ' + self.squares[0] + ' | ' + self.squares[1] + ' | ' + self.squares[2] + ' |')
        print(separator)
        print('| ' + self.squares[3] + ' | ' + self.squares[4] + ' | ' + self.squares[5] + ' |')
        print(separator)
        print('| ' + self.squares[6] + ' | ' + self.squares[7] + ' | ' + self.squares[8] + ' |')
        print(separator)
        pass

    # waits for the next player to choose a square
    def player_turn(self, player):
        square = int(input(player + ': Choose a square [1 - 9]\n'))
        if self.squares[square - 1] != ' ':
            print('That square has already been chosen\n')
            self.player_turn(player)
        if player == 'p1':
            self.squares[square - 1] = 'X'
            self.player_up_next = 'p2'
        else:
            self.squares[square - 1] = 'O'
            self.player_up_next = 'p1'
        self.draw_board()
        self.check_victory()

    def check_victory(self):
        x_squares = []
        o_squares = []
        # iterate through all the squares, check to see if they're X or O and add results to a list
        for i in range(len(self.squares)):
            if self.squares[i] == 'X':
                x_squares.append(i)
            if self.squares[i] == 'O':
                o_squares.append(i)
        winner = self.win_check(x_squares, o_squares)
        if winner == 'X Wins!' or winner == "O Wins!":
            self.end_game()
        self.player_turn(self.player_up_next)
        pass

    def win_check(self, x, o):
        # winning scenarios
        if 0 in x and 1 in x and 2 in x:
            self.players.update_score('p1')
            print('X Wins!')
            return 'X Wins!'
        if 0 in o and 1 in o and 2 in o:
            self.players.update_score('p2')
            print('O Wins!')
            return 'O Wins!'
        if 0 in x and 3 in x and 6 in x:
            self.players.update_score('p1')
            print('X Wins!')
            return 'X Wins!'
        if 0 in o and 3 in o and 6 in o:
            self.players.update_score('p2')
            print('O Wins!')
            return 'O Wins!'
        if 0 in x and 4 in x and 8 in x:
            self.players.update_score('p1')
            print('X Wins!')
            return 'X Wins!'
        if 0 in o and 4 in o and 8 in o:
            self.players.update_score('p2')
            print('O Wins!')
            return 'O Wins!'
        if 1 in x and 4 in x and 7 in x:
            self.players.update_score('p1')
            print('X Wins!')
            return 'X Wins!'
        if 1 in o and 4 in o and 7 in o:
            self.players.update_score('p2')
            print('O Wins!')
            return 'O Wins!'
        if 2 in x and 5 in x and 8 in x:
            self.players.update_score('p1')
            print('X Wins!')
            return 'X Wins!'
        if 2 in o and 5 in o and 8 in o:
            self.players.update_score('p2')
            print('O Wins!')
            return 'O Wins!'
        if 2 in x and 4 in x and 6 in x:
            self.players.update_score('p1')
            print('X Wins!')
            return 'X Wins!'
        if 2 in o and 4 in o and 6 in o:
            self.players.update_score('p2')
            print('O Wins!')
            return 'O Wins!'
        if 3 in x and 4 in x and 5 in x:
            self.players.update_score('p1')
            print('X Wins!')
            return 'X Wins!'
        if 3 in o and 4 in o and 5 in o:
            self.players.update_score('p2')
            print('O Wins!')
            return 'O Wins!'
        if 6 in x and 7 in x and 8 in x:
            self.players.update_score('p1')
            print('X Wins!')
            return 'X Wins!'
        if 6 in o and 7 in o and 8 in o:
            self.players.update_score('p2')
            print('O Wins!')
            return 'O Wins!'
        both = x+o
        if len(both) == 9:
            self.players.update_score('tie')
            print('The game was a Tie')
            self.end_game()
        pass

    def end_game(self):
        # TODO Terminate the application
        print('Scores:')
        print('Player 1: ' + self.players.get_score('p1') + ' wins')
        print('Player 2: ' + self.players.get_score('p2') + ' wins')
        print('Ties: ' + str(self.players.ties) + '\n')
        if input('Would you like to play another game? yes or no\n') == 'yes':
            self.begin_game()
        else:
            print('Game Ended - Final Scores')
            print('Player 1: ' + self.players.get_score('p1') + ' wins')
            print('Player 2: ' + self.players.get_score('p2') + ' wins')
            print('Ties: ' + str(self.players.ties) + '\n')
            exit()
        pass
    pass
