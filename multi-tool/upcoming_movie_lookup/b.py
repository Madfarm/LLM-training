def upcoming_movie_lookup(movies, month_year):
    current_month_year = datetime.now().strftime('%B %Y')
    if current_month_year == month_year:
        movies = [movie for movie in movies if movie['release_date'] == month_year]
    else:
        movies = [movie for movie in movies if movie['release_date'] > current_month_year]
    return movies

movies = [
    {"title": "A Quiet Place: Day One", "cast": ["Lupita Nyong'o", "Joseph Quinn", "Djimon Hounsou", "Alex Wolff"], "release_date": "November 2024"},
    {"title": "Gladiator 2", "cast": ["Denzel Washington", "Pedro Pascal", "Connie Nielsen", "Paul Mescal"], "release_date": "November 2024"},
    {"title": "Kung Fu Panda 4", "cast": ["Jack Black", "Awkwafina", "Viola Davis", "Dustin Hoffman"], "release_date": "December 2024"}
]

lookup_month = "November 2024"
print(upcoming_movie_lookup(movies, lookup_month))