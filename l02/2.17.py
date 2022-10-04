# Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości. Wskazówka: funkcja wbudowana sorted().

import re

line = "Ex officia sint minim reprehenderit GvR proident Lorem adipisicing ex. Et commodo excepteur eu Lorem non non. GvR Non et proident velit tempor sunt labore ullamco Lorem aliquip magna."


words = re.split('\s+', line)

alpha = sorted(words)
lengths = sorted(words,key=lambda x: len(x))

print(alpha)
print(lengths)