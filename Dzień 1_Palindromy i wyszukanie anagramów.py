"""#PALINDROMY I #ANAGRAMY
Napisz program, który prosi użytkownika o podanie dowolnego napisu. Następnie program wyświetla na ekranie to słowo
wspak (od prawej do lewej) i wyświetla komunikat czy to wyrażenie jest palindromem (czyli czytane wspak daje do samo
wyrażenie np. “ala”, “Kobyła ma mały bok” (inne przykłady: http://www.palindromy.pl/pal_kr.php). Podczas sprawdzania
ignoruj wielkość liter oraz znaki niebędące literami. Następnie wywołaj dowolną stronę internetową, która pokaże
anagramy oraz słowa utworzone po usunięciu liter, np. https://poocoo.pl/scrabble-slowa-z-liter/hardcoder

Propozycja rozszerzenia: samodzielnie wyszukaj anagramy i słowa utworzone po usunięciu liter z podanego słowa, na
przykład wykorzystując słownik wspomniany na stronie https://anagramy.wybornie.com/ """

import webbrowser
import time
def ask_phrase():
    check_phrase = input('Podaj tekst, który może być palindromem\n')
    return check_phrase

def remove_punctuation(phrase):
    new_phrase = ''
    for char in phrase:
        if char.isalpha() == True:
            new_phrase += char
    return new_phrase

def check_palindrome(phrase):
    print('Wpisana fraza zapisana od tyłu: {}'.format(phrase[::-1]))
    if phrase.lower() == phrase[::-1].lower():
        print('Ten łańcuch znaków jest palindromem')
        print('Wyszukuję słowa możliwe do uzyskania poprzez mieszanie liter:')
        time.sleep(2)
        webbrowser.open(url='https://poocoo.pl/scrabble-slowa-z-liter/{}'.format(phrase))
        print('Sprawdź okno przeglądarki')
    elif phrase != phrase[::-1]:
        print('To nie jest palindrom')


if __name__ == '__main__':
    phrase = ask_phrase()
    phrase = remove_punctuation(phrase)
    check_palindrome(phrase)