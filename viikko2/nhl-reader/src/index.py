from rich.console import Console
from rich.table import Table

from player import PlayerReader, PlayerStats

BASE_URL = "https://studies.cs.helsinki.fi/nhlstats"
SEASONS = (
    "2018-19",
    "2019-20",
    "2020-21",
    "2021-22",
    "2022-23",
    "2023-24",
    "2024-25",
    "2025-26",
    "2026-27",
)


def choose_season():
    print("Choose a season:")
    for number, season in enumerate(SEASONS, start=1):
        print(f"{number}. {season}")

    while True:
        selection = input("Season number: ").strip()
        try:
            season_index = int(selection) - 1
        except ValueError:
            season_index = -1

        if 0 <= season_index < len(SEASONS):
            return SEASONS[season_index]

        print(f"Please enter a number from 1 to {len(SEASONS)}.")


def choose_nationality(nationalities):
    available_nationalities = set(nationalities)
    print(f"Available nationality codes: {', '.join(available_nationalities)}")

    while True:
        nationality = input("Nationality: ")
        if nationality in available_nationalities:
            return nationality
        print("Please enter one of the listed nationality codes.")


def choose_team(teams):
    available_teams = set(teams)
    print(f"Available teams: {', '.join(sorted(available_teams))}")

    while True:
        team = input("Team: ").strip()
        if team in available_teams:
            return team
        print("Please enter one of the listed teams.")


def choose_player_filter():
    print("Choose how to filter players:")
    print("1. Nationality")
    print("2. Team")

    while True:
        selection = input("Selection: ").strip()
        if selection == "1":
            return "nationality"
        if selection == "2":
            return "team"
        print("Please enter 1 or 2.")


def build_table(season, filter_value):
    table = Table(title=f"Top scorers: {filter_value} ({season})")
    table.add_column("Rank", justify="right")
    table.add_column("Player")
    table.add_column("Team")
    table.add_column("GP", justify="right")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right", style="bold")
    return table

def display_players(players, season, filter_value, console):
    table = build_table(season, filter_value)

    for rank, player in enumerate(players, start=1):
        table.add_row(
            str(rank),
            player.name,
            player.team,
            str(player.games),
            str(player.goals),
            str(player.assists),
            str(player.score),
        )

    console.print(table)


def select_players(stats, all_players):
    player_filter = choose_player_filter()

    if player_filter == "team":
        teams = {player.team for player in all_players}
        filter_value = choose_team(teams)
        players = stats.top_scorers_by_team(filter_value)
    else:
        nationalities = {player.nationality for player in all_players}
        filter_value = choose_nationality(nationalities)
        players = stats.top_scorers_by_nationality(filter_value)

    return filter_value, players


def main():
    season = choose_season()
    url = f"{BASE_URL}/{season}/players"
    reader = PlayerReader(url)
    all_players = reader.get_players()
    stats = PlayerStats(all_players)
    filter_value, players = select_players(stats, all_players)

    display_players(players, season, filter_value, Console())

if __name__ == "__main__":
    main()
