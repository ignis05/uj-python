# Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na napis.

import random

liczba = random.randint(10000000000000000, 99999999999999999)

count = str(liczba).count('0')

print(liczba)
print(count)
