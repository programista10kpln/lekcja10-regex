import re

# match, search, findall i sub

wzor = r'pilka'
tekst = r'lodowka pilka kosz stol pilka pilka'

print(re.match(wzor, tekst))  # szuka od początku

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
