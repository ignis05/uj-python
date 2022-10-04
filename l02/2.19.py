# Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie.
# Chcemy zbudować napis z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024.
# Wskazówka: str.zfill().

import random

L = [1, 10, 100] + random.sample(range(1, 999), 20)
napis = ', '.join([str(nr).zfill(3) for nr in L])

print(L)
print(napis)
