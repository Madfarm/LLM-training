from datetime import date

def upcoming_movie_lookup(movie_list, month_year):
    current_month = int(date.today().strftime("%m"))
    current_year = int(date.today().strftime("%Y"))

    #convert the input month_year to tuple
    month, year = map(int, month_year.split('/'))
    
    filtered_list = [] 

    for movie in movie_list:
        release_month, release_year = movie['Release Date']
        # Check if the movie's release date is in the future
        if release_year > current_year or release_year == current_year and release_month > current_month:
            filtered_list.append(movie)

    movies = [movie for movie in filtered_list if movie['Release Date'] == (month, year)]
    return movies

movie_list = [
    {"Title": "Despicable Me 4", "Cast": ["Steve Carell", "Kristen Wiig", "Miranda Cosgrove", "Pierre Coffin", "Chris Renaud", "Will Ferrell", "Joey King"], "Release Date": (7, 2024)},  
    {"Title": "Sound of Hope: The Story of Possum Trot", "Cast": ["Not specified"], "Release Date": (6, 2024)},
    {"Title": "Twisters", "Cast": ["Daisy Edgar-Jones", "Glen Powell", "Anthony Ramos", "Maura Tierney", "Katy O’Brian"], "Release Date": (7, 2024)},
    {"Title": "Minions: The Rise of Gru", "Cast": ["Steve Carell", "Alan Arkin", "Taraji P. Henson", "Lucy Aarden", "Derek Drymon"], "Release Date": (7, 2022)},
]  
month_year = '07/2024'
print(upcoming_movie_lookup(movie_list, month_year))  