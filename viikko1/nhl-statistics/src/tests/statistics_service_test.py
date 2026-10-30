import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_returns_player(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 37)
        self.assertEqual(player.assists, 53)

    def test_search_returns_none(self):
        player = self.stats.search("Selänne")

        self.assertEqual(player, None)

    def test_team_returns_players(self):
        team = self.stats.team("EDM")

        self.assertEqual(len(team), 3)

    def test_top_returns_right_amount_of_players(self):
        top = self.stats.top(3)

        self.assertEqual(len(top), 4)

    def test_top_returns_players_in_right_order_without_sorting(self):
        top = self.stats.top(3)

        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Lemieux")
        self.assertEqual(top[2].name, "Yzerman")

    def test_top_returns_players_in_right_order_by_points(self):
        top = self.stats.top(3, sort_by=StatisticsService.SortBy.POINTS)

        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Lemieux")
        self.assertEqual(top[2].name, "Yzerman")

    def test_top_returns_players_in_right_order_by_goals(self):
        top = self.stats.top(3, sort_by=StatisticsService.SortBy.GOALS)

        self.assertEqual(top[0].name, "Lemieux")
        self.assertEqual(top[1].name, "Yzerman")
        self.assertEqual(top[2].name, "Kurri")

    def test_top_returns_players_in_right_order_by_assists(self):
        top = self.stats.top(3, sort_by=StatisticsService.SortBy.ASSISTS)

        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Yzerman")
        self.assertEqual(top[2].name, "Lemieux")