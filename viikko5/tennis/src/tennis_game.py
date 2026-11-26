class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_point(self):
        self.score += 1

class TennisGame:
    SCORE_DICT = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
    
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if self.player1.name == player_name:
            self.player1.add_point()
        else:
            self.player2.add_point()

    def even_score(self, score):
        if score == 0:
            return "Love-All"
        elif score == 1:
            return "Fifteen-All"
        elif score == 2:
            return "Thirty-All"
        else:
            return "Deuce"

    def score_diff_advantage(self, score1, score2):
            score_diff = score1 - score2
            if score_diff == 1:
                return "Advantage player1"
            elif score_diff == -1:
                return "Advantage player2"
            elif score_diff >= 2:
                return "Win for player1"
            else:
                return "Win for player2"

    def get_score(self):
        if self.player1.score == self.player2.score:
            return self.even_score((self.player1.score))

        elif self.player1.score >= 4 or self.player2.score >= 4:
            return self.score_diff_advantage(self.player1.score, self.player2.score)

        else:
            return f"{self.SCORE_DICT[self.player1.score]}-{self.SCORE_DICT[self.player2.score]}"
