"""#PASSWORD #GENERATOR
Napisz program do generowania losowych haseł o zadanej przez użytkownika długości. Hasło musi spełniać zadane warunki
 np. co najmniej jedna liczba, co najmniej po jednej dużej i małej literze. Warto skorzystać z modułów string i secrets.
Propozycja rozszerzenia: Po wygenerowaniu hasła skopiuj je do schowka systemowego """

import random
import string
import pyperclip


def pass_generating(pass_length):  # Password. Standard: At least one digit and one punctuation
    temp_pass = ""
    characters = string.ascii_letters + string.punctuation + string.digits
    while len(temp_pass) < pass_length:
        temp_pass += random.choice(characters)  # Random choice of the passwords' characters till given length
    if any(c in string.punctuation for c in temp_pass):  # Check if there's at least one punctuation and one digit
        if any(c in string.digits for c in temp_pass):
            return temp_pass
    return pass_generating(pass_length)


if __name__ == '__main__':
    pass_length = int(input('How many characters do you want your password to have?\n'))
    password = pass_generating(pass_length)
    pyperclip.copy(password)  # Copy password ready for pasting