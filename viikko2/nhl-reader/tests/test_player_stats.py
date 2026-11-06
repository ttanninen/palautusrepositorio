import unittest

from player import Player, PlayerStats


class PlayerReaderStub:  # pylint: disable=too-few-public-methods
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


class PlayerStatsTest(unittest.TestCase):
    def setUp(self):
        players = [
            Player({
                "name": "Alex",
                "nationality": "CAN",
                "assists": 28,
                "goals": 20,
                "team": "BOS",
                "games": 50,
            }),
            Player({
                "name": "Blair",
                "nationality": "USA",
                "assists": 10,
                "goals": 35,
                "team": "BOS",
                "games": 50,
            }),
            Player({
                "name": "Casey",
                "nationality": "CAN",
                "assists": 15,
                "goals": 25,
                "team": "DAL",
                "games": 50,
            }),
            Player({
                "name": "Devon",
                "nationality": "CAN",
                "assists": 20,
                "goals": 10,
                "team": "BOS",
                "games": 50,
            }),
            Player({
                "name": "Eden",
                "nationality": "USA",
                "assists": 40,
                "goals": 5,
                "team": "DAL",
                "games": 50,
            }),
        ]
        reader = PlayerReaderStub(players)
        self.players = reader.get_players()
        self.stats = PlayerStats(self.players)

    def test_return_players_returns_stub_players(self):
        self.assertEqual(self.stats.return_players(), self.players)

    def test_top_goal_scorers_returns_n_players_by_goals(self):
        result = self.stats.top_goal_scorers(2)

        self.assertEqual([player.name for player in result], ["Blair", "Casey"])

    def test_top_scorers_by_nationality_filters_and_sorts_by_points(self):
        result = self.stats.top_scorers_by_nationality("CAN")

        self.assertEqual([player.name for player in result], ["Alex", "Casey", "Devon"])

    def test_top_scorers_by_team_filters_and_sorts_by_points(self):
        result = self.stats.top_scorers_by_team("BOS")

        self.assertEqual([player.name for player in result], ["Alex", "Blair", "Devon"])


if __name__ == "__main__":
    unittest.main()
