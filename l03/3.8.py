# Dla dwóch sekwencji liczb lub znaków znaleźć:
# (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
# (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).


sequence1 = [1, 2, 3, 4]
sequence2 = [2, 3, 4, 5]


def intersection(seq1, seq2):
    s1 = set(seq1)
    s2 = set(seq2)
    return list(s1.intersection(s2))


def union(seq1, seq2):
    s1 = set(seq1)
    s2 = set(seq2)
    return list(s1.union(s2))
    


print('a', intersection(sequence1, sequence2))
print('b', union(sequence1, sequence2))
