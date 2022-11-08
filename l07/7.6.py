# Stworzyć następujące iteratory nieskończone:
# (a) zwracający 0, 1, 0, 1, 0, 1, ...,
# (b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],
# (c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].
import itertools
import random

iter_a = itertools.cycle([0, 1])
iter_b = iter((lambda: random.choice(("N", "E", "S", "W"))), 1)
iter_c = itertools.cycle([x for x in range(7)])


res_a, res_b, res_c = [], [], []
for i in range(20):
    res_a.append(next(iter_a))
    res_b.append(next(iter_b))
    res_c.append(next(iter_c))

print(f"a: {str(res_a)}")
print(f"b: {str(res_b)}")
print(f"c: {str(res_c)}")
