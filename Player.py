"""
Object to keep track of the players.
Tracks their number of wins, updates number of wins, and returns number of wins
"""
class player:
    def __init__(self):
        self.p1_wins = 0
        self.p2_wins = 0
        self.ties = 0
        pass

    def update_score(self, outcome):
        if outcome == 'p1':
            self.p1_wins += 1
        if outcome == 'p2':
            self.p2_wins += 1
        if outcome == 'tie':
            self.ties += 1
        pass

    def get_score(self, player):
        if player == 'p1':
            return str(self.p1_wins)
        if player == 'p2':
            return str(self.p2_wins)
        pass

    def return_scores(self):
        return self.p1_wins, self.p2_wins, self.ties
        pass
