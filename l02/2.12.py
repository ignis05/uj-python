# Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line. Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.

import re

line = """Pierwsze zdanie w wielowierszowym napisie.  
Drugie zdanie w nowej linijce
Ostatnia linijka"""

words = re.split('\s+', line)

print(' '.join([word[0] for word in words]))
print(' '.join([word[-1] for word in words]))
