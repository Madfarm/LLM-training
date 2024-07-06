def calculate_points(player_stats, games):
    points_per_game = player_stats['points_per_game']
    assists_per_game = player_stats['assists_per_game']
    total_points = points_per_game * games
    total_assists = assists_per_game * games
    total_points += total_assists * 2  # assuming each assist is worth 2 points
    return f"{player_stats['name']} would earn his team a total of {total_points} in {games} games."

# usage
player_stats = {
    'name': 'Nikola Jokic',
    'points_per_game': 26.4,
    'assists_per_game': 9.0
}

games = 125
print(calculate_points(player_stats, games))