import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.games = dict['games']
        self.id = dict['id']

        self.score = self.goals + self.assists

    def __str__(self):
        return (
            f"{self.name:25} {self.team:15} "
            f"{self.assists:3} + {self.goals:3} = {self.score:3}"
        )

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        players = [Player(player_dict) for player_dict in response]
        return players


class PlayerStats:
    def __init__(self, players):
        self.players = players

    def top_scorers_by_nationality(self, nationality):
        players_by_nationality = [
            player for player in self.players if player.nationality == nationality
        ]
        return sorted(players_by_nationality, key=lambda player: player.score, reverse=True)