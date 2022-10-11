def add_poly(poly1: list, poly2: list):        # poly1(x) + poly2(x)
    long, short = (poly1.copy(), poly2.copy()) if len(poly1) >= len(poly2) else (poly2.copy(), poly1.copy())
    for i, x in enumerate(short):
        long[i] += x
    return long


def sub_poly(poly1: list, poly2: list):        # poly1(x) - poly2(x)
    l1 = poly1.copy()
    l2 = poly2.copy()
    while (len(l1) < len(l2)):
        l1.append(0)
    for i, x in enumerate(l1):
        if i < len(l2):
            l1[i] -= l2[i]
    return l1


def mul_poly(poly1: list, poly2: list):     # poly1(x) * poly2(x)
    long, short = (poly1.copy(), poly2.copy()) if len(poly1) >= len(poly2) else (poly2.copy(), poly1.copy())
    result = [0]
    for i, x in enumerate(short):
        result = add_poly(result, [0 for a in range(i)] + [b*x for b in long])
    return result


def is_zero(poly: list):                 # bool, [0], [0,0], itp.
    for x in poly:
        if x != 0:
            return False
    return True


def eq_poly(poly1: list, poly2: list):        # bool, porównywanie poly1(x) == poly2(x)
    l1 = poly1.copy()
    l2 = poly2.copy()
    while (len(l1) < len(l2)):
        l1.append(0)
    while (len(l2) < len(l1)):
        l2.append(0)

    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True


def eval_poly(poly: list, x0: float):           # poly(x0), algorytm Hornera
    result = False
    for x in reversed(poly):
        if not result:
            result = x
            continue
        result = result*x0 + x

    return result


def combine_poly(poly1: list, poly2: list): pass    # poly1(poly2(x)), trudne!


def pow_poly(poly: list, n: int):             # poly(x) ** n
    if n == 0:
        return 1
    if n == 1:
        return poly
    result = poly.copy()
    for i in range(n-1):
        result = mul_poly(result, poly)
    return result


def diff_poly(poly: list):               # pochodna wielomianu
    result = []
    for i, x in enumerate(poly):
        if i == 0:
            continue
        result.append(i*x)
    return result
