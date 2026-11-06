from player import PlayerReader, PlayerStats

URL = "https://studies.cs.helsinki.fi/nhlstats/2026-27/players"
reader = PlayerReader(URL)
stats = PlayerStats(reader.get_players())

for p in stats.top_scorers_by_team("DAL"):
    print(p)
