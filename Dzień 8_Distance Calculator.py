"""#DISTANCE #CALCULATOR
Napisz program liczący odległość liniową między dwoma dowolnymi punktami na mapie, wykorzystujący ich współrzędne
geograficzne (długość i szerokość geograficzną). Wykorzystaj dowolny algorytm, np.
https://pl.wikibooks.org/.../Astrono.../Odleg%C5%82o%C5%9Bci
Skorzystaj z API (np. https://rapidapi.com/trueway/api/trueway-geocoding), żeby obliczyć odległość pomiędzy twoim
adresem, a charakterystycznymi punktami np. Wieżą Eiffla czy Tadź Mahal.
Propozycja rozszerzenia: zamiast podawać swój adres, użyj geolokalizacji """

import requests
import math
import json

def provide_data():
    address = input('Please enter the address\n')
    country = input('Please enter the country code (two letters, e.g.: PL)\n')
    return address, country

def request_data(address, country, language='en'):
    url = "https://trueway-geocoding.p.rapidapi.com/Geocode"
    querystring = {"address": address, "language": "en", "country": country}
    headers = {
        'x-rapidapi-key': "XXXXX",
        'x-rapidapi-host': "trueway-geocoding.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = json.loads(response.text)
    return response

def get_geolocation(data):
    lat = data['results'][0]['location']['lat']
    lon = data['results'][0]['location']['lng']
    return lat, lon


def calculate_distance(lattiude_start, longtitude_start, lattiude_end, longtitude_end):  # Calculate the distance. Curvature of globe is not considered
    distance = math.sqrt((lattiude_start - lattiude_end)**2 + (math.cos(lattiude_end * math.pi/180) *
                                                               (longtitude_start - longtitude_end))**2) * (40075.704 / 360)
    return distance


if __name__ == '__main__':
    print('Please provide the address of the first (start) point')
    address_start = provide_data()
    requested_data_start = request_data(address_start[0], address_start[1])
    location_start = get_geolocation(requested_data_start)
    print('Please provide the address of the second (end) point')
    address_end = provide_data()
    requested_data_end = request_data(address_end[0], address_end[1])
    location_end = get_geolocation(requested_data_end)
    distance = calculate_distance(location_start[0], location_start[1], location_end[0], location_end[1])
    print(distance)




