import random
import getpass

print("Gra papier kamien i nozyce")
ilosc_rund = int(input("podaj ilosc rund: "))


tryb = 0
while tryb not in range (1,3):
    tryb = int(input("podaj numer trybu \n 1. dwoch graczy \n 2. gra z komputerem \n"))

pl_1 = ""
pl_2 = ""

if tryb == 1:
    pl_1 = input("podaj nazwe pierwszego gracza: ")
    pl_2 = input("podaj nazwe drugiego gracza: ")
elif tryb == 2:
    pl_1 = input("podaj swoja nazwe gracza: ")
    pl_2 = "cpu"

round_counter = 0
opcje = ['p', 'k', 'n']

while round_counter < 10:
    print("nr rundy: ", round_counter+1)

    print("Ruch gracza: ", pl_1)
    print("Wybierz ruch wpisujac litere opcji \n p - papier \n k - kamien \n n - nozyce")
    ruch_pl_1 = getpass.getpass('wybor: ')

    if tryb == 1:
        print("Ruch gracza: ", pl_2)
        print("Wybierz ruch wpisujac litere opcji \n p - papier \n k - kamien \n n - nozyce")
        ruch_pl_2 = getpass.getpass('wybor: ')

    else:
        print("cpu")
        rand = random.randint(1,3)
        ruch_pl_2 = opcje[rand]


    print("pl_1 ", ruch_pl_1)
    print("pl_2 ", ruch_pl_2)











