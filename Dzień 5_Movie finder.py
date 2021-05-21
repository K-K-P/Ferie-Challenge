"""#MOVIE #FINDER
Przy wykorzystaniu API (np. IMDB) wyszukaj wszystkie części filmu zadanego w wyszukiwaniu (np. Rambo, Scary Movie,
Shrek). Można przyjąć założenie, że wszystkie filmy “z serii” muszą zawierać szukany ciąg - czasem zdarzają się błędne
wyniki wyszukiwania z baz, można je spróbować odfiltrować. Wyświetl dla każdego podstawowe informacje np. rok,
długość, ocena, spis aktorów (pierwszych 5 z listy).
Przykładowe API do wykorzystania:
https://rapidapi.com/apidojo/api/imdb8/endpoints - do wyszukania filmów z daną nazwą (do odfiltrowania można użyć
warunku, że dany rekord posiada nazwę i rok wydania)
https://rapidapi.com/.../imdb-internet-movie-database... - pobranie szczegółów o danym filmie"""

import requests
import json

def connection(movie_title):
    url = "https://imdb8.p.rapidapi.com/auto-complete"
    querystring = {"q": "{}".format(movie_title)}
    headers = {
        'x-rapidapi-key': "XXXXXXXXX",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

def data_acquisition(data):
    data_acquire = {'l': 'Movie title', 'y': 'Release year', 'rank': 'Rank', 's': 'Starring'}  # Parameters (keys) to acquire
    for i in range(len(data['d'])):  # 'd' is the main key in dictionary
        for d in data_acquire:  # iter over keys to acquire
            try:
                print('{}: '.format(data_acquire[d]), data['d'][i][d])  # Print the data of movies
            except KeyError:
                pass
        print('-------------')




#print(response.text)
if __name__ == '__main__':
    movie = input('Please type the title of the movie that you\'d like to search for\n')
    response = connection(movie)
    if response.status_code == 200:
        data = json.loads(response.text)
        #print(data)
        data_acquisition(data)
    else:
        print('Incorrect data - please check the input and try again')
