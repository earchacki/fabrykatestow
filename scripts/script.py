import random

liczba = random.randint(1,10)

print('Wylosowana liczba to : ', liczba)

# listy (tablice)
lista = ['kołdra', 'krzesło', 'stół', 'żyrandol']
print(lista)
print(lista[1:3])

# słowniki
slownik = {'kuchnia': ['kuchenka', 'garnki', 'sztućce'], 'łazienka':['ręczniki', ' szampon', 'suszarka']}
print(slownik)
print(slownik['kuchnia'][1], slownik['łazienka'])

# zmienne
resztaZdzielenia = 11 % 3
print(resztaZdzielenia)

potega = 3 ** 2
print(potega)

mnozenieStringa = 'joł ' * 2
print(mnozenieStringa * 3)

#dodawanie List
lista1 = [2, 4, 6, 8]
lista2 = [1, 3, 5, 7]
sumaList = lista1 + lista2
print(sumaList)

imie = 'Roman'
wiek = 55

if imie in ('Piotr', 'Roman') and wiek == 55:
    print('Joł Roman')
else:
    print('kto ty?')


liczba1 = 1
liczba2 = 2

if liczba1 > 5:
    print(1)
elif liczba2 >5:
    print(2)
else:
    print('same false')

# range(od której zacząć, na której zakończyć -1, o ile przyrost)
for i in range(11, 15, 2):
    print(i)

licznik = 0
while licznik < 3:
    print('while', licznik)
    licznik += 1

licznik = 0
while True:
    print('break', licznik)
    licznik += 1
    if licznik == 3:
        break

for x in range(6):
    if x % 2 == 0:      # parzyste wyłapuje i je drukuje-  gdy reszta jest 0
        print('continue', x)
        continue

for x in range(6):
    if x % 2 == 0:      # parzyste wyłapuje i je pomija
        continue
    print('continue2', x)