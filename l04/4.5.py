# Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie.
# Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.

lista1 = [i for i in range(0, 20)]


def odwracanie(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
        
def odwracanieR(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanieR(L, left+1, right-1)

print(lista1)
odwracanie(lista1, 10, 15)
print(lista1)
odwracanieR(lista1, 10, 15)
print(lista1)
