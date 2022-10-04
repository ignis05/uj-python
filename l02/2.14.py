# Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.

import re


line = """Pierwsze zdanie w wielowierszowym napisie.  
Drugie zdanie w nowej linijce
Ostatnia linijka"""

words = re.split('\s+', line)

longestWord = words[0]
wordLen = len(longestWord)

for word in words:
    l = len(word)
    if l > wordLen:
        longestWord = word
        wordLen = l

print(f'(a): {longestWord}\n(b): {wordLen}')
