class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_point(self):
        self.score += 1

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def point(self, point):
        point_dict = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
        return point_dict[point]

    def won_point(self, player_name):
        if self.player1.name == player_name:
            self.player1.add_point()
        else:
            self.player2.add_point()

    def even_score(self, score):
        if score >= 3:
            return "Deuce"
        else:    
            return self.point(score) + "-All"

    def score_diff_advantage(self, player1, player2):
        if player1.score > player2.score:
            leader = player1
        else:
            leader = player2

        score_diff = player1.score - player2.score
        if abs(score_diff) == 1:
            return "Advantage " + leader.name
        elif abs(score_diff) >= 2:
            return "Win for " + leader.name

    def get_score(self):
        if self.player1.score == self.player2.score:
            return self.even_score((self.player1.score))

        elif self.player1.score >= 4 or self.player2.score >= 4:
            return self.score_diff_advantage(self.player1, self.player2)

        else:
            return f"{self.point(self.player1.score)}-{self.point(self.player2.score)}"
