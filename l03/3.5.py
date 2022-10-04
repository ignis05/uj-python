# Napisać program rysujący "miarkę" o zadanej długości.
# Należy prawidłowo obsłużyć liczby składające się z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej).
# Należy zbudować pełny string, a potem go wypisać.
# |....|....|....|....|....|....|....|....|....|....|....|....|
# 0    1    2    3    4    5    6    7    8    9   10   11   12

dl = int(input('Podaj dl miarki:\n'))

uRow = '|'
lRow = '0'

for i in range(1, dl+1):
    uRow += '....|'
    lRow += str(i).rjust(5, ' ')

result = uRow + '\n' + lRow

print(result)
