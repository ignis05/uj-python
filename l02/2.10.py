# Mamy dany napis wielowierszowy line. Podać sposób obliczenia liczby wyrazów w napisie.
# Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).
import re


line = """Pierwsze zdanie w wielowierszowym napisie.  
Drugie zdanie w nowej linijce
Ostatnia linijka"""


wordCount = len(re.split('\s+', line))
print(wordCount)
