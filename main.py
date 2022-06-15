def powitanie():
    global imie
    imie = str(input((r'''
______
|    |
|    O
|   /|\
|   / \    Witaj w grze Wisielec!
|
|          Wpisz nazwę gracza: ''')))


def pozegnanie():
    print(r'''
______
|    |
|    O
|   /|\
|   / \    Do zobaczenia następnym razem!
|
|''')


def zmien_gracza():
    global imie
    imie = str(input('\nWpisz nazwę gracza: '))
    menu()


def menu():
    print('\nWitaj ', imie, '! Wybierz co chcesz zrobić:\n[1] Zacznij grę\n[2] Zobacz statystyki\n[3] Zmień gracza\n[4] Wyjdż z programu',
          sep='')
    menu = input('Wpisz liczbę: ')
    while not menu.isdecimal():
        menu = input('Niepoprawne dane, wpisz liczbę od 1 do 4: ')
        while menu.isdecimal() and int(menu) not in range(1, 5):
            menu = input('Niepoprawne dane, wpisz liczbę od 1 do 4: ')
    menu = int(menu)
    if menu == 1:
        zacznij_gre()
    elif menu == 2:
        statystyki()
    elif menu == 3:
        zmien_gracza()
    else:
        pozegnanie()


def zacznij_gre():
    print('\n[1] Wybierz kategorię\n[2] Dodaj własną kategorię\n[3] Powrót do menu')
    zacznij = input('Wpisz liczbę: ')
    while not zacznij.isdecimal():
        zacznij = input('Niepoprawne dane, wpisz liczbę od 1 do 3: ')
        while zacznij.isdecimal() and int(zacznij) not in range(1, 4):
            zacznij = input('Niepoprawne dane, wpisz liczbę od 1 do 3: ')
    zacznij = int(zacznij)
    if zacznij == 1:
        wybierz_kategorie()
    elif zacznij == 2:
        dodaj_kategorie()
    elif zacznij == 3:
        menu()


def wybierz_kategorie():
    import datetime
    print('\nDostępne kategorie:\n[1] zwierzęta\n[2] astronomia\n[3] sport\n\n[0] Powrót do menu')
    kategoria = input('Wpisz liczbę: ')
    while not kategoria.isdecimal():
        kategoria = input('Niepoprawne dane, wpisz liczbę od 0 do 3: ')
        while kategoria.isdecimal() and int(kategoria) not in range(0, 4):
            kategoria = input('Niepoprawne dane, wpisz liczbę od 0 do 3: ')
    kategoria = int(kategoria)
    if kategoria != 0:
        wybierz_jezyk(kategoria)
    else:
        menu()


def wybierz_jezyk(kategoria):
    print('\nDostępne języki:\n[1] polski\n[2] angielski\n[3] francuski\n\n[0] Powrót do menu')
    jezyk = input('Wpisz liczbę: ')
    while not jezyk.isdecimal():
        jezyk = input('Niepoprawne dane, wpisz liczbę od 0 do 3: ')
        while jezyk.isdecimal() and int(jezyk) not in range(0, 4):
            jezyk = input('Niepoprawne dane, wpisz liczbę od 0 do 3: ')
    jezyk = int(jezyk)
    if jezyk != 0:
        losowanie(jezyk, kategoria)
    else:
        menu()


def losowanie(jezyk, kategoria):
    import random
    kategoria -= 1
    if jezyk == 1:
        kategorie = [
        ['wielbłąd', 'kanarek', 'mrówka', 'pszczoła', 'niedźwiedź', 'aligator', 'żmija', 'antylopa', 'pawian', 'kozioł',
         'kameleon', 'szympans', 'gepard', 'krowa', 'jeleń', 'mucha', 'sarna', 'delfin', 'osioł', 'kaczka', 'flaming',
         'żyrafa', 'pasikonik', 'jastrząb', 'hipopotam', 'iguana', 'biedronka', 'jaszczurka', 'świstak', 'małpa',
         'ośmiornica', 'pantera', 'pingwin', 'bażant', 'świnia', 'modliszka', 'nosorożec', 'salamandra', 'wiewiórka'],

        ['meteoryt', 'galaktyka', 'konstelacja', 'mgławica', 'supernowa', 'orbita', 'ekliptyka', 'Słońce', 'Księżyc',
         'Merkury', 'Wenus', 'Ziemia', 'Mars', 'Jowisz', 'Saturn', 'Uran', 'Neptun', 'Pluton', 'Andromeda', 'Kasjopeja',
         'Perseusz'],

        ['akrobatyka', 'arbiter', 'badminton', 'bieżnia', 'capoeira', 'tenis', 'siatkówka', 'pływactwo', 'karate',
         'deskorolka', 'dogrywka', 'futbol', 'drybling', 'falstart', 'gimnastyka', 'golf', 'hokej', 'hipodrom', 'boks',
         'jeździectwo', 'kajakarstwo', 'łyżwiarstwo', 'narciarstwo', 'nokaut', 'olimpiada', 'piruet', 'pilates']]
        slowo = random.choice(kategorie[kategoria]).upper()
        wybierz_trudnosc(slowo)

    elif jezyk == 2:
        kategorie = [
        ['camel', 'antelope', 'baboon', 'goat', 'chimpanzee', 'octopus', 'mantis', 'penguin'],

        ['Moon', 'Sun', 'Jupiter', 'nebula', 'meteorite', 'Earth', 'Mercury', 'Venus', 'Cassiopeia'],

        ['acrobatics', 'basketball', 'volleyball', 'swimming', 'canoeing', 'gymnastics']]
        slowo = random.choice(kategorie[kategoria]).upper()
        wybierz_trudnosc(slowo)

    elif jezyk == 3:
        kategorie = [
        ['chameau', 'antilope', 'babouin', 'poulpe', 'manchot', 'coccinelle', 'marmotte', 'cochon'],

        ['Lune', 'Soleil', 'Jupiter', 'nébuleuse', 'Terre', 'Mercure', 'Cassiopeia', 'galaxie'],

        ['acrobaties', 'natation', 'gymnastique', 'tennis', 'golf', 'pirouette', 'hockey']]
        slowo = random.choice(kategorie[kategoria]).upper()
        wybierz_trudnosc(slowo)


def wybierz_trudnosc(slowo):
    print('\nWybierz poziom trudności:\n[1] Łatwy - 10 prób, 2 podpowiedzi\n[2] Normalny - 8 prób, 1 podpowiedź\n[3] Trudny - 5 prób, 0 podpowiedzi\n\n[0] Powrót do menu')
    trudnosc = input('Wpisz liczbę: ')
    while not trudnosc.isdecimal():
        trudnosc = input('Niepoprawne dane, wpisz liczbę od 0 do 3: ')
        while trudnosc.isdecimal() and int(trudnosc) not in range(0, 4):
            trudnosc = input('Niepoprawne dane, wpisz liczbę od 0 do 3: ')
    trudnosc = int(trudnosc)
    if trudnosc == 1:
        pozostale_proby = 10
        podpowiedz = 2
        gra(slowo, pozostale_proby, podpowiedz)
    elif trudnosc == 2:
        pozostale_proby = 8
        podpowiedz = 1
        gra(slowo, pozostale_proby, podpowiedz)
    elif trudnosc == 3:
        pozostale_proby = 5
        podpowiedz = 0
        gra(slowo, pozostale_proby, podpowiedz)
    else:
        menu()


def gra(slowo, pozostale_proby, podpowiedz):
    import random
    print(slowo)
    postep_gry = '_' * len(slowo)
    podane_litery = []
    czy_wygrana = False
    while pozostale_proby > 0:
        print('\nTwoje słowo:', postep_gry, '\nAby skorzystać z podpowiedzi wpisz 0.')
        proba = input('Podaj literę lub słowo: ').upper()
        if proba == '0':
            if podpowiedz != 0:
                losowa_litera = random.choice(slowo)
                while losowa_litera in podane_litery:
                    losowa_litera = random.choice(slowo)
                podane_litery += losowa_litera
                postep_gry = ''
                for litera in slowo:
                    if litera in podane_litery:
                        postep_gry += litera
                    else:
                        postep_gry += '_'
                if slowo in postep_gry:
                    print('\nGratulacje, wygrałeś grę! Poprawna odpowiedź to ', slowo, '.', sep='')
                    czy_wygrana = True
                    zmiana_statystyk(czy_wygrana)
                    ponowna_gra()
                    break
                podpowiedz -= 1
            else:
                print('\nNie masz więcej podpowiedzi!')
        elif len(proba) == 1 and proba.isalpha():
            if proba in podane_litery:
                print('\nTa litera została podana wcześniej, spróbuj ponownie.')
            elif proba not in slowo:
                podane_litery += proba
                wisielec(pozostale_proby)
                pozostale_proby -= 1
            else:
                podane_litery += proba
                postep_gry = ''
                for litera in slowo:
                    if litera in podane_litery:
                        postep_gry += litera
                    else:
                        postep_gry += '_'
                if slowo in postep_gry:
                    print('\nGratulacje, wygrałeś grę! Poprawna odpowiedź to ', slowo, '.', sep='')
                    czy_wygrana = True
                    zmiana_statystyk(czy_wygrana)
                    ponowna_gra()
                    break
        elif len(proba) == len(slowo) and proba.isalpha():
            if proba == slowo:
                print('\nGratulacje, wygrałeś grę! Poprawna odpowiedź to ', slowo, '.', sep='')
                czy_wygrana = True
                zmiana_statystyk(czy_wygrana)
                ponowna_gra()
                break
            else:
                wisielec(pozostale_proby)
                pozostale_proby -= 1
        else:
            print('Niepoprawne dane, spróbuj ponownie.')
    if pozostale_proby == 0:
        print('\nNiestety, tym razem przegrałeś. Poprawna odpowiedź to ', slowo, '.', sep='')
        zmiana_statystyk(czy_wygrana)
        ponowna_gra()


def wisielec(pozostale_proby):
    if pozostale_proby == 10:
        print(r'''


|
|
|
|''')
    if pozostale_proby == 9:
        print(r'''|
|
|
|
|
|
|''')
    elif pozostale_proby == 8:
        print(r'''
______
|
|
|
|
|
|''')
    elif pozostale_proby == 7:
        print(r'''
______
|    |
|
|
|
|
|''')
    elif pozostale_proby == 6:
        print(r'''
______
|    |
|    O
|
|
|
|''')
    elif pozostale_proby == 5:
        print(r'''
______
|    |
|    O
|    |
|
|
|''')
    elif pozostale_proby == 4:
        print(r'''
______
|    |
|    O
|   /|
|
|
|''')
    elif pozostale_proby == 3:
        print(r'''
______
|    |
|    O
|   /|\
|
|
|''')
    elif pozostale_proby == 2:
        print(r'''
______
|    |
|    O
|   /|\
|   /
|
|''')
    elif pozostale_proby == 1:
        print(r'''
______
|    |
|    O
|   /|\
|   / \
|
|''')


def ponowna_gra():
    ponownie = input('\nCzy chciałbyś zagrać ponownie?\n[1] Tak!\n[2] Nie, wyjdź z gry.\nWpisz liczbę: ')
    while not ponownie.isdecimal():
        ponownie = input('Niepoprawne dane, wpisz liczbę od 1 do 2: ')
        while ponownie.isdecimal() and int(ponownie) not in range(1, 4):
            ponownie = input('Niepoprawne dane, wpisz liczbę od 1 do 2: ')
    ponownie = int(ponownie)
    if ponownie == 1:
        zacznij_gre()
    else:
        pozegnanie()


def statystyki():
    import csv
    try:
        statystyki = open('statystyki.csv', 'r', newline='')
        statystykiReader = csv.reader(statystyki)
        print('')
        for linia in statystykiReader:
            print(linia[0].ljust(20), linia[1].ljust(20), linia[2].ljust(20))
        statystyki.close()
    except:
        statystyki=open('statystyki.csv', 'w', newline='')
        statystykiWriter = csv.writer(statystyki)
        statystykiWriter.writerow(['Gracz', 'Ilość wygranych', 'Ilość przegranych'])
        print('Gracz'.ljust(20), 'Ilość wygranych'.ljust(20), 'Ilość przegranych'.ljust(20))
        statystyki.close()
    wybor = input('Kliknij enter żeby powrócić do menu: ')
    menu()


def zmiana_statystyk(czy_wygrana):
    import csv
    try:
        statystyki = open('statystyki.csv', 'r', newline='')
        statystykiReader = csv.reader(statystyki)
        statystyki_temp = []
        for linia in statystykiReader:
            statystyki_temp += [linia]
        statystyki.close()

        statystyki = open('statystyki.csv', 'w', newline='')
        statystykiWriter = csv.writer(statystyki)
        statystykiWriter.writerow(statystyki_temp[0])

        gracze = []
        for linia in range(1, len(statystyki_temp)):
            gracze += [statystyki_temp[linia][0]]

        if imie in gracze:
            for linia in range(1, len(statystyki_temp)):
                if statystyki_temp[linia][0] == imie:
                    if czy_wygrana == True:
                        statystykiWriter.writerow([imie, int(statystyki_temp[linia][1]) + 1, statystyki_temp[linia][2]])
                    else:
                        statystykiWriter.writerow([imie, statystyki_temp[linia][1], int(statystyki_temp[linia][2]) + 1])
                else:
                    statystykiWriter.writerow([statystyki_temp[linia][0], statystyki_temp[linia][1], statystyki_temp[linia][2]])
        else:
            for linia in range(1, len(statystyki_temp)):
                statystykiWriter.writerow([statystyki_temp[linia][0], statystyki_temp[linia][1], statystyki_temp[linia][2]])

            if czy_wygrana == True:
                statystykiWriter.writerow([imie, 1, 0])
            else:
                statystykiWriter.writerow([imie, 0, 1])

    except:
        statystyki = open('statystyki.csv', 'w', newline='')
        statystykiWriter = csv.writer(statystyki)
        statystykiWriter.writerow(['Gracz', 'Ilość wygranych', 'Ilość przegranych'])
        if czy_wygrana == True:
            statystykiWriter.writerow([imie, 1, 0])
        else:
            statystykiWriter.writerow([imie, 0, 1])
    finally:
        statystyki.close()


def dodaj_kategorie():
    import random
    try:
        print('\nAby dodać własną listę słów, podaj ścieżkę do pliku. Pamiętaj, aby słowa były odzielone tylko przecinkiem (bez spacji)!\nPrzykładowy format listy słów: Afryka,Europa,Australia,Azja\nAby wrócić do menu, kliknij enter.')
        sciezka=input('Podaj ścieżkę: ')
        plik=open(sciezka, 'r')
        kategoria = plik.read().split(',')
        plik.close()

        slowo = random.choice(kategoria).upper()
        wybierz_trudnosc(slowo)
    except:
        print('\nNiepoprawna ścieżka, wracam do menu.')
        menu()


def main():
    powitanie()
    menu()

main()