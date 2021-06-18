"""#SUMMARY
Napisz program, który odczytuje wszystkie pliki stworzone przez Ciebie podczas #feriechallenge - przeszukuje lokalne
 katalogi lub łączy się w tym celu z Githubem. Postaraj się jak najmniej hardcodować i na przykład nie podawaj listy
 wszystkich plików ręcznie 🙂  Następnie wykorzystując swój sposób katalogowania programów automat odczytuje i
 wyświetla takie informacje:
-> do ilu zadań z 10 napisało się kod
-> liczba linijek kodu napisanych w każdym zadaniu (bez uwzględniania pustych!) oraz sumaryczna liczba linijek
-> liczba unikalnych słów użytych we wszystkich programach oraz najczęściej występujące słowo
-> lista i liczba słów kluczowych użyta podczas całego challenge (wykorzystaj moduł keywords)
-> lista i liczba zaimportowanych modułów we wszystkich programach
Propozycja rozszerzenia: Po prostu miej odwagę i pochwal się outputem swojego programu! - opublikuj posta z
tagiem #feriechallenge i zostaw lajka na naszej stronie, będzie nam miło 🙂 Możesz też oczywiście umieścić jakieś
dodatkowe statystyki."""

import os
from string import ascii_letters
from collections import Counter

files_counter = 0
lines_counter = 0
words = []

for root, dirs, file in os.walk(os.getcwd()):
    files = [f for f in file if '.py' in f]  # Receive only Python files

    for f in files:
        if 'Dzień' in f:
            files_counter += 1
            with open(f, 'rb') as f:
                for line in f.readlines():
                    line = line.decode(encoding='UTF-8').replace('\n', '').replace('\r', '') # decode from bytes type
                    line.lstrip()
                    lines_counter += 1
                    line_list = line.split(' ')
                    line_list = [word for word in line_list if len(word) > 0] # Filter for spaces
                    line_list = [word for word in line_list if word[0] in ascii_letters] # Filter for non alfanum
                    words.extend(line_list)


print('You\'ve managed to complete {} out of 10 projects. It took {} lines of code to achieve it.'.format(files_counter,
                                                                                                          lines_counter))
count = Counter(words)
print('The most common phrase / word used in Your projects was: "{}"'.format(count.most_common(1)[0][0]))

