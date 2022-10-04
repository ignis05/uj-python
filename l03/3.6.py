# Napisać program rysujący prostokąt zbudowany z małych kratek.
# Należy zbudować pełny string, a potem go wypisać. Przykładowy prostokąt składający się 2x4 pól ma postać:

# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+

height = int(input('height: '))
width = int(input('width: '))

result = ''

for h in range((height*2)+1):
    for w in range((width*2)+1):
        if h % 2 == 0:
            result += '+' if w % 2 == 0 else '---'
        else:
            result += '|' if w % 2 == 0 else '   '
    result += '\n'

print(result)
