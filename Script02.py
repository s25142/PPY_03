import random


miasta = ['Warszawa', 'Kraków', 'Wrocław', 'Łódź', 'Poznań', 'Gdańsk', 'Szczecin', 'Bydgoszcz', 'Lublin', 'Torun', 'Bialystok', 'Rzeszów', 'Gdynia']

for x in range (0, 10):
    r = random.randint(0, len(miasta)-1)
    print(x+1, ". ",miasta[r])

    miasta.remove(miasta[r])

