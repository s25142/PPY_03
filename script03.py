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
    pl_2 = "CPU"

round_counter = 0
opcje = ['p', 'k', 'n']

opcje_map = {
    'p': 'papier',
    'k': 'kamien',
    'n': 'nozyce'
}
rounds_result = []

while round_counter < ilosc_rund:
    print("\nnr rundy: ", round_counter+1)

    print("Ruch gracza: ", pl_1)
    print("Wybierz ruch wpisujac litere opcji \n p - papier \n k - kamien \n n - nozyce")
    ruch_pl_1 = getpass.getpass('wybor: ')

    if tryb == 1:
        print("Ruch gracza: ", pl_2)
        print("Wybierz ruch wpisujac litere opcji \n p - papier \n k - kamien \n n - nozyce")
        ruch_pl_2 = getpass.getpass('wybor: ')

    else:
        rand = random.randint(0,2)
        ruch_pl_2 = opcje[rand]


    print(pl_1, opcje_map[ruch_pl_1])
    print(pl_2, opcje_map[ruch_pl_2])

    round_result = [0,0]

    if ruch_pl_1 == ruch_pl_2:
        print("remis")
        round_result[0] += 1
        round_result[1] += 1
    elif ruch_pl_1 == 'p':
        if ruch_pl_2 == 'k':
            print("runde wygrywa gracz ", pl_1)
            round_result[0] += 1
        else:
            print("runde wygrywa gracz ", pl_2)
            round_result[1] += 1
    elif ruch_pl_1 == 'k':
        if ruch_pl_2 == 'n':
            print("runde wygrywa gracz ", pl_1)
            round_result[0] += 1
        else:
            print("runde wygrywa gracz ", pl_2)
            round_result[1] += 1
    elif ruch_pl_1 == 'n':
        if ruch_pl_2 == 'p':
            print("wygrywa gracz ", pl_1)
            round_result[0] += 1
        else:
            print("wygrywa gracz ", pl_2)
            round_result[1] += 1

    rounds_result.append(round_result)

    round_counter += 1

print('\n\n')
sum_pl1 = 0
sum_pl2 = 0
for x in rounds_result:
    sum_pl1 += x[0]
    sum_pl2 += x[1]

if(sum_pl1 == sum_pl2):
    print("gra zakonczona remisem")
    print("wynik gracza ", pl_1, sum_pl1)
    print("wynik gracza ", pl_2, sum_pl2)
elif (sum_pl1 > sum_pl1):
    print("gre wygrywa ", pl_1)
    print("wynik gracza ", pl_1, sum_pl1)
    print("wynik gracza ", pl_2, sum_pl2)
else:
    print("gre wygrywa ", pl_2)
    print("wynik gracza ", pl_1, sum_pl1)
    print("wynik gracza ", pl_2, sum_pl2)

c = 1
print("\n lista wynikow")
for x in rounds_result:
    print("runda ", c," ",x)
    c += 1










