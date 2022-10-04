# Znaleźć łączną długość wyrazów w napisie line. Wskazówka: można skorzystać z funkcji sum().

import re


line = """Pierwsze zdanie w wielowierszowym napisie.  
Drugie zdanie w nowej linijce
Ostatnia linijka"""

words = re.split('\s+', line)

print(sum([len(word) for word in words]))