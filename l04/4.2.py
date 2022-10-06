# Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, które zwracają pełny string przez return.
# Funkcje nie powinny pytać użytkownika o dane, tylko korzystać z argumentów.

def make_ruler(n):
    uRow = '|'
    lRow = '0'

    for i in range(1, n+1):
        uRow += '....|'
        lRow += str(i).rjust(5, ' ')

    return uRow + '\n' + lRow


def make_grid(rows, cols):
    result = ''

    for h in range((rows*2)+1):
        for w in range((cols*2)+1):
            if h % 2 == 0:
                result += '+' if w % 2 == 0 else '---'
            else:
                result += '|' if w % 2 == 0 else '   '
        result += '\n'

    return result


print(make_ruler(15))
print(make_grid(5, 8))
