from datetime import date

def upcoming_movie_lookup(movie_list, month_year):
    current_month = int(date.today().strftime("%m"))
    current_year = int(date.today().strftime("%Y"))

    filtered_list = []
    # Convert the input month_year to a tuple for comparison
    month_year_tuple = (int(month_year[0]), int(month_year[1]))
    
    for movie in movie_list:
        release_date = movie["Release Date"]
        if release_date > (current_month, current_year):
            filtered_list.append(movie)
 
    movies = [movie for movie in filtered_list if movie['Release Date'] == month_year_tuple]
    return movies


movie_list = [
    {"Title": "Despicable Me 4", "Cast": ["Steve Carell", "Kristen Wiig"], "Release Date": (7, 2024)},  
    {"Title": "Sound of Hope", "Cast": ["Not specified"], "Release Date": (6, 2024)},  
    {"Title": "Twisters", "Cast": ["Daisy Edgar-Jones"], "Release Date": (5, 2024)},
    {"Title": "Future Movie", "Cast": ["Tomorrow's Actors"], "Release Date": (8, 2024)}
]

# Let's check the movies for July 2024
print(upcoming_movie_lookup(movie_list, ("7", "2024")))  