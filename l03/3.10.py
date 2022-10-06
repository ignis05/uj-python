# Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie (podać kilka sposobów tworzenia takiego słownika).
# Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].


# moznaby tez miec pelen slownik tlumaczacy wyrazenia z prefixami np IV=4, albo nawet caly alfabet 1:1 z zapisami w stylu: II=2, III=3
romanDict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def roman2int(roman):
    romanList = [romanDict[x] for x in roman]
    result = 0
    lastVal = 10001
    for nr in romanList:
        result += nr
        # if previous value smaller than current, it should've been subtracted instead of added - correct
        if lastVal < nr:
            result -= 2*lastVal
        lastVal = nr
    return result


for val in ['XX', 'XIX', 'IV', 'III', 'LXXXII', 'XCIX']:
    print(f'{val} = {roman2int(val)}')
