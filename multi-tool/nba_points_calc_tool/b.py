def calculate_points(player_stats, games):
    points = player_stats['points'] * games
    assists = player_stats['assists'] * games
    total_points = points + assists * 2
    return total_points

def output(player_name, total_points, games):
    print(f"{player_name} would earn his team a total of {total_points} in {games} games.")

player_stats = {'points': 26.4, 'assists': 9.0}
games = 125
total_points = calculate_points(player_stats, games)
output('Nikola Jokic', total_points, games)