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
