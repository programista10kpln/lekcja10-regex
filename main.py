import re

# match, search, findall i sub

wzor = r'pilka'
tekst = r'lodowka pilka kosz stol pilka pilka'

print(re.match(wzor, tekst))  # szuka od początku (domyślnie)

if re.match(r'.*' + wzor + r'.*', tekst):
    print('dopasowano')
else:
    print('nie dopasowano')

if re.search(wzor, tekst):  # szuka w całym tekście
    print('dopasowano')
else:
    print('nie dopasowano')

print(re.findall(wzor, tekst))  # zwraca listę wszystkich wystąpień

szukanie = re.search(wzor, tekst)
if szukanie:
    print(szukanie.group())
    print(szukanie.start())
    print(szukanie.end())
    print(szukanie.span())
tekst2 = re.sub(wzor, r'boisko', tekst)  # podmienia
print(tekst2)

print('\n')  # zaawansowane wzory

if re.match('^[^A-Za-g]o.$', 'rot'):
    print('dopasowano')
else:
    print('nie dopasowano')

print('\n')  # więcej operatorów

if re.match('^[A-Z]$', 'H'):
    print('dopasowano')
else:
    print('nie dopasowano')

if re.match(r'^([^\.]+)(@)([^\.]+)(\.)([^\.]{2,})$', 'user@o2.pl'):
    print('dobry e-mail')
else:
    print('to nie e-mail')

print('\n')  # grupy - nawiasy

wynik = re.match(r'^(?P<first>Hello) (World)$', 'Hello World')
if wynik:
    print(wynik.group(0))
    print(wynik.group('first'))
    print(wynik.groups())
else:
    print('nie dopasowano')

print('\n')  # argumenty funkcji - lista parametrów (krotka)


def funkcja(arg1, arg2='World', *args, **kwargs):
    return arg1, arg2, args, kwargs


# jedna gwiazdka to nieskonczona ilosc argumentow, a dwie gwiazdki wymagja takze etykiety, bo to tworzy słownik

print((funkcja('Hi', 'Poland')))
print((funkcja('Hi', 'Poland', ':)', ':D', dzien='Poniedziałek', rok='2022')))

print('\n')  # rozpakowanie krotki

a, b = (2, 5)
print(a)
print(b)

x = 7
y = 20
x, y = y, x
print(f'x: {x}')
print(f'y: {y}')

start, *wszystko, koniec, koniec2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(start)
print(wszystko)
print(koniec)
print(koniec2)

# gwiazdka bierze te nieprzypisane

print('\n')  # skrócony if

print('prawda') if 5 > 2 else print('nieprawda')

a = 'parzysta' if 5 % 2 == 0 else 'nieparzysta'
print(a)

for i in range(1, 10):
    if i > 5:
        print(i)
        continue
else: # dziala po koncu petli, nie liczac break
    print('koniec')
try:
    a = 5/0
except ZeroDivisionError:
    print('nie dzielimy przez 0')
else: # dziala gdy nie ma bledu
    print('koniec')
finally:
    print('zawsze bede na ekranie ;)')