"""Stwórz prosty program, który będzie wysyłał spersonalizowany mailing do wybranych osób. “Bazą danych” jest plik
Excela (aby było “ciekawiej” 😉 ) lub CSV, zawierający dwie kolumny z nagłówkami: “E-mail” oraz “Imię i nazwisko”
(zakładamy, że zawsze w takiej kolejności, a imię i nazwisko są oddzielone spacją). Do użytkowników należy wysłać maila
z tematem “Your image” oraz spersonalizowaną prostą treścią np. “Hi {Imię}! it’s file generated for you”. Dodatkowo
w załączniku maila znajduje się plik graficzny o nazwie “{Imię}_{Nazwisko}_image.png” (pliki są w zadanej lokalizacji).
 Odpowiednio zabezpiecz program (np. brakujący plik Excela, brakujące dane w Excelu, brak pliku png) oraz
 zabezpiecz przed spamowaniem (np. jeden mail wysyłany co 1 sekundę). Mogą przydać się moduły: smtplib, email, ssl,
xlrd, re, os.
Propozycje rozszerzenia: dodaj opcję wysyłania maili z treścią w HTML oraz walidator poprawności maila (np. używając
wyrażeń regularnych - moduł re)."""

import openpyxl
import time
import smtplib
from email.message import EmailMessage


def read_cell(sheet_object, cell_adress):
    return sheet_object[cell_adress].value  # Read the cell's content


def split_name(name):
    name_list = name.split(' ')
    return name_list


def create_message(to_name, to_address, me='xxxx'):
    msg = EmailMessage()  # Message object
    msg['Subject'] = 'Your image, {}'.format(to_name)
    msg['From'] = me
    msg['To'] = to_address
    msg.set_content('Hi, {}! It\'s a file generated for you'.format(to_name))  # Set content of a message (raw string?)
    with open('image.png', 'rb') as image:
        msg.add_attachment(image.read(), maintype='image', subtype='png')  # Add an attachment
    return msg


def send_message(message, password, host='smtp.gmail.com', port='587', user='xxxx'):
    with smtplib.SMTP(host, port) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user, password)
        server.send_message(message)
        server.quit()


wb = openpyxl.load_workbook('Lista mailingowa.xlsx', read_only=True)  # Open the Excel file
sheet = wb['Arkusz1']  # Sheet content to variable
flag = True  # Flag for while loop
cell_index = 2  # Starting index for iteration over cells
validation_counter = 0  # Counter fol mail validation
password = input('Please provide mail password in order to send files\n')
while flag:
    mail_address = read_cell(sheet, 'A{}'.format(cell_index))  # Read mail address
    if mail_address:
        name = split_name(read_cell(sheet, 'B{}'.format(cell_index)))[0]  # Read receiver's name
        if name:
            print(mail_address, name)
            send_message(create_message(name, mail_address), password)
            time.sleep(2)
        elif not name:
            print('Receiver\'s data missing')
            pass
    else:
        validation_counter += 1
    if validation_counter >= 3:
        flag = False
    cell_index += 1






