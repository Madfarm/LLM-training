from datetime import date

def upcoming_movie_lookup(movie_list, month_year):
    current_month = int(date.today().strftime("%m"))
    current_year = int(date.today().strftime("%Y"))

    filtered_list = []
    for movie in movie_list:
        release_month, release_year = movie["Release Date"]
        if release_year > current_year or (release_year == current_year and release_month > current_month):
            filtered_list.append(movie)

    movies = [movie for movie in filtered_list if movie['Release Date'] == month_year]
    return movies

# Example usage:
movie_list = [
    {"Title": "A Quiet Place: Day One", "Cast": ["Lupita Nyong'o", "Joseph Quinn", "Djimon Hounsou", "Alex Wolff"], "Release Date": (11, 2024)},
    {"Title": "Gladiator 2", "Cast": ["Denzel Washington", "Pedro Pascal", "Connie Nielsen", "Paul Mescal"], "Release Date": (11, 2024)},
    {"Title": "Kung Fu Panda 4", "Cast": ["Jack Black", "Awkwafina", "Viola Davis", "Dustin Hoffman"], "Release Date": (12, 2024)},
]

month_year = (11, 2024)
print(upcoming_movie_lookup(movie_list, month_year))

month_year = (7, 2024)
movie_list = [
    {"Title": "Despicable Me 4", "Cast": ["Steve Carell", "Kristen Wiig", "Miranda Cosgrove", "Pierre Coffin", "Chris Renaud", "Will Ferrell", "Joey King"], "Release Date": (7, 2024)},
    {"Title": "Sound of Hope: The Story of Possum Trot", "Cast": ["Not specified"], "Release Date": (7, 2024)},
    {"Title": "Twisters", "Cast": ["Daisy Edgar-Jones", "Glen Powell", "Anthony Ramos", "Maura Tierney", "Katy O’Brian"], "Release Date": (7, 2024)},
]
print(upcoming_movie_lookup(movie_list, month_year))