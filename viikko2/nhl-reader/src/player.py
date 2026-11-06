import requests

class Player:
    def __init__(self, catalog):
        self.name = catalog['name']
        self.nationality = catalog['nationality']
        self.assists = catalog['assists']
        self.goals = catalog['goals']
        self.team = catalog['team']
        self.games = catalog['games']
        self.id = catalog.get('id')

        self.score = self.goals + self.assists

    def return_score(self):
        return self.score

    def __str__(self):
        return (
            f"{self.name:25} {self.team:15} "
            f"{self.assists:3} + {self.goals:3} = {self.score:3}"
        )

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def return_url(self):
        return self.url

    def get_players(self):
        response = requests.get(self.url, timeout=10).json()
        players = [Player(player_dict) for player_dict in response]
        return players


class PlayerStats:
    def __init__(self, players):
        self.players = players

    def return_players(self):
        return self.players

    def top_goal_scorers(self, n=10):
        """Palauttaa n parasta maalintekijää pelaajalistan perusteella."""
        return sorted(self.players, key=lambda player: player.goals, reverse=True)[:n]

    def top_scorers_by_nationality(self, nationality):
        players_by_nationality = [
            player for player in self.players if player.nationality == nationality
        ]
        return sorted(players_by_nationality, key=lambda player: player.score, reverse=True)

    def top_scorers_by_team(self, team):
        players_by_team = [player for player in self.players if player.team == team]
        return sorted(players_by_team, key=lambda player: player.score, reverse=True)
