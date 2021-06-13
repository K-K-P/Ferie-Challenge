"""#HOUSE #LIBRARY
Napisz program, który importuje katalog z dowolnej biblioteki (np. API Biblioteki Narodowej http://data.bn.org.pl/ -
przykład użycia: http://data.bn.org.pl/api/bibs.json...). Użytkownik może podać autora i program pokaże mu, jakie
książki tego autora są w zbiorach biblioteki. Następnie daj użytkownikowi możliwość “wypożyczania” i “zwracania” książek
 - posiadane pozycje są składowane w pliku zawierającym pewien identyfikujący zbiór danych, np. tytuł, autor,
 wydawnictwo, rok wydania (możesz też użyć lokalnej bazy danych), w przypadku “wypożyczenia” książki są do niego
 dodawane, a w przypadku “zwracania” usuwane.
Propozycja rozszerzenia: W prostym przypadku lokalne “wypożyczanie” nie ma wpływu na katalog biblioteki, czyli w teorii
można wypożyczyć książkę nieskończoną liczbę razy. Zabezpiecz program w taki sposób, aby podczas pobierania danych
 rozpoznawał też pozycje “wypożyczone” lokalnie i nie pokazywał ich już jako wyniki wyszukiwania."""

import requests
import json
import shelve  # Using shelve module to make it sql-free solution


def request_data(author, title, limit = 5):  # Function to acquire data, limit - number of occurences on one page (default = 5)
    url = 'http://data.bn.org.pl/api/authorities.json'
    params = {'limit': limit, 'author': author, 'title': title}
    response = requests.request('GET', url, params=params)
    data = json.loads(response.text)
    return data


def request_next(url):  # Request another page of data
    response = requests.request('GET', url)
    data_next = json.loads(response.text)
    return data_next


def request_book(pos_id, data):  # Updating lend book database
    with shelve.open('Collections') as db:
        db.update({pos_id: [data[pos_id]['Title'], data[pos_id]['Author']]})


def return_book(book_id):  # Returning the book / deleting from shelve database
    with shelve.open('Collections') as db:
        db.pop(str(book_id))
        print('Position {} returned'.format(str(book_id)))


def database_list():
    with shelve.open('Collections') as db:
        for k in db:
            print('{}: {}, {}'.format(k, db.get(k)[0], db.get(k)[1]))


def next_page(page):  # Function for accessing further pages (if existing)
    next_data = request_next(page)
    if next_data['authorities']:
        page_data = next_data['authorities']
    else:
        page_data = []
    page = next_data['nextPage']
    return page_data, page


def searching():
    print('Please provide the data')
    author = input('Author: ')
    title = input('Title: ')
    if author and title:
        data = request_data(author, title)
        combine_data = data['authorities']
        page = data['nextPage']
        while page:
            output = next_page(page)
            page = output[1]
            data = output[0]
            combine_data.extend(data)
        listing = {}
        for d in combine_data:  # Combining all available entries into one nested dictionary
            listing[str(d['id'])] = {'Author': d['name'], 'Title': d['title']}
        print('Please find below the list of result\n')
        for k in listing.keys():
            print(k, listing[k]['Author'], listing[k]['Title'], sep='|')

    else:
        print('Provided data are not complete, please try again\n')
        searching()
    return listing


if __name__ == '__main__':
    print('''Welcome to National Library!\n''')
    flow_control = True
    while flow_control:
        function = input('What would you like to do now: '
                         '[C]heck through your positions? / [S]earch through our library? / [Q]uit? / [R]eturn postion? /'
                         '[B]orrow a book?\n')
        if function.lower() == 'q':
            flow_control = False
        elif function.lower() == 's':
            listing = searching()
        elif function.lower() == 'c':
            database_list()
        elif function.lower() == 'r':
            flag_1 = True
            while flag_1:
                book_id = input('Please provide the ID of the book that you want to return: ')
                with shelve.open('Collections') as db:
                    if book_id in db.keys():
                        return_book(book_id)
                        return_again = input('Would you like to return another position? (Y/N)\n')
                        if return_again.lower() == 'n':
                            flag_1 = False
                    else:
                        print('ID not in your collection. Please check the number and try again')
        elif function.lower() == 'b':
            flag_1 = True
            while flag_1:
                book_id = input('Please provide the ID of the book that you want to borrow: ')
                with shelve.open('Collections') as db:
                    if book_id not in db.keys():
                        request_book(book_id, listing)
                        return_again = input('Would you like to return another position? (Y/N)\n')
                        if return_again.lower() == 'n':
                            flag_1 = False
                    else:
                        print('ID already in your collection. Please check the number and try again')
                    out = input('Finish operation? (Y \\ N)\n')
                    if out.lower() == 'y':
                        flag_1 = False
                    elif out.lower() == 'n':
                        pass














