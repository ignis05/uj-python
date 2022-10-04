# Na liście L znajdują się liczby całkowite dodatnie. Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.

import random

L = random.sample(range(1, 100), 15)


napis = ''.join([str(n) for n in L])

print(L)
print(napis)
