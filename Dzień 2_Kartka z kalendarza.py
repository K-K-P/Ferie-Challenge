"""#feriechallenge #program2
Wczoraj poradziliście sobie świetnie! 🙂 No to dzisiaj trochę podkręcamy poziom, żeby nie było nudno 😎
(ale drodzy początkujący, spokojnie! poziomy będą oscylować, a nie tylko iść do góry!) 🦸‍♀️🦸‍♂️
Dzisiaj proponujemy pokorzystać trochę z API i zaciągnąć trochę danych "na żywo" (proponowane przez nas rapidapi ma tą
zaletę, że jest darmowe po założeniu konta oraz można od razu pobrać snippety kodu w danym języku - ale można korzystać
oczywiście z dowolnego źródła i techniki, web scrapping też dozwolony!). Jeśli ktoś ma dużo czasu zawsze można też
do tej bajki dołozyć wizualizację 🤩
#KARTKA #Z #KALENDARZA
Napisz program, który po uruchomieniu wyświetla w czytelnej formie aktualną datę, godzinę, dzień tygodnia
i pogodę/temperaturę/ciśnienie w zadanym mieście (wykorzystaj np. https://rapidapi.com/commu.../api/open-weather-map/endpoints
- pamiętaj o poprawnym przeliczeniu jednostek np. temperatura z kelwinów na stopnie) oraz losowy cytat
(np. https://type.fit/api/quotes ). Wykorzystaj requests i datetime.
Propozycja rozszerzenia: Wyświetl również bieżący czas dla miast w różnych strefach czasowych (np. Pekin, Sydney,
Waszyngton, Londyn) - wykorzystaj np. pytz: https://pypi.org/project/pytz/ oraz wyświetl listę osób obchodzących
imieniny (poszukaj otwartej bazy danych lub wykorzystaj prosty web scrapping np. z wykorzystaniem:
https://imienniczek.pl/widget/js )."""

import requests
import json
import datetime
import random
import bs4
import re

city = input('Which city\'s weather would you like to check?\n').lower()
weatherURL = 'https://api.weatherbit.io/v2.0/current'
weatherParams = {'city': city,
          'key': '45d6f653bdcf44c882162b39e20d4b96'}

quotesURL = 'https://type.fit/api/quotes'

def connection(url, method="GET", params=''):
    response = requests.request(method, url, params=params)
    return response


def weather(url, params):
    response = connection(url, params=params)
    if str(response) == '<Response [200]>':
        data = json.loads(response.text)
        forecast = data['data'][0]
        print('Current time:', str(datetime.datetime.now())[:16])
        print('Weather for: {}'.format(forecast['city_name']))
        print('Current temperature: {} deg C'.format(forecast['temp']))
        print('Current pressure: {} kPa'.format(forecast['pres']))
        print('Cloud cover: {}\n'.format(forecast['weather']['description']))
    else:
        print('There was an error while connection. Please check correctness of city\'s name and try again')
        return

def randomQuotes(url, params=''):
    response = connection(url, params=params)
    if str(response) == '<Response [200]>':
        data = json.loads(response.text)
        quoteData = random.choice(data)
        print('Today\'s quote by {} is:'.format(quoteData['author']))
        print('"{}"\n'.format(quoteData['text']))

def nameDay():
    imieniny = requests.get('https://imienniczek.pl')
    soup = bs4.BeautifulSoup(imieniny.text, 'html.parser')
    solenizant = soup.select('html.h-100 body.d-flex.flex-column.h-100 main.container.m-div aside div.box div#txt_d.box_txt table.box_tab')
    p = re.compile('>\w+<')
    listNames = p.findall(str(solenizant))
    print('Today a reason to celebrate have:\n')
    for name in listNames:
        print(name[1:-1])


if __name__ == '__main__':
    weather(weatherURL, weatherParams)
    randomQuotes(quotesURL)
    nameDay()
