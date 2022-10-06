# Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone podsekwencje.
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

def sum_seq(sequence):
    result = 0
    for item in sequence:
        result += sum_seq(item) if isinstance(item, (list, tuple)) else item
    return result


seq = [[], [4], (1, 2), [3, [4, 5, 6]], (5, 6, 7)]

print(sum_seq(seq))