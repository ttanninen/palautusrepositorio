class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_point(self):
        self.score += 1

class TennisGame:
    POINT_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    POINTS_TO_WIN = 4
    ADVANTAGE = 1

    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def point(self, point):
        return self.POINT_NAMES[point]

    def won_point(self, player_name):
        if self.player1.name == player_name:
            self.player1.add_point()
        else:
            self.player2.add_point()

    def get_score(self):
        if self.player1.score == self.player2.score:
            return self._even_score((self.player1.score))

        elif max(self.player1.score, self.player2.score) >= self.POINTS_TO_WIN:
            return self._endgame_score(self.player1, self.player2)

        else:
            return self._normal_score(self.player1, self.player2)

    def _even_score(self, score):
        if score >= len(self.POINT_NAMES) - 1:
            return "Deuce"    
        return self.point(score) + "-All"

    def _endgame_score(self, player1, player2):
        leader = player1 if player1.score > player2.score else player2
        score_diff = abs(player1.score - player2.score)
        
        if score_diff == self.ADVANTAGE:
            return "Advantage " + leader.name
        return "Win for " + leader.name

    def _normal_score(self, player1, player2):
        return f"{self.point(player1.score)}-{self.point(player2.score)}"