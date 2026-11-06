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


def build_table(season, nationality):
    table = Table(title=f"Top scorers: {nationality} ({season})")
    table.add_column("Rank", justify="right")
    table.add_column("Player")
    table.add_column("Team")
    table.add_column("GP", justify="right")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right", style="bold")
    return table

def display_players(players, season, nationality, console):
    table = build_table(season, nationality)

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

def main():
    season = choose_season()
    url = f"{BASE_URL}/{season}/players"
    reader = PlayerReader(url)
    all_players = reader.get_players()
    nationalities = sorted({player.nationality for player in all_players})
    nationality = choose_nationality(nationalities)
    stats = PlayerStats(all_players)
    players = stats.top_scorers_by_nationality(nationality)

    display_players(players, season, nationality, Console())

if __name__ == "__main__":
    main()
