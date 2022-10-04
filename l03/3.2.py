# Co jest złego w kodzie:

# %%
L = [3, 5, 4] ; L = L.sort()
# list.sort() sortuje w miejscu i zwraca None, przypisanie do L psuje kod

# %%
x, y = 1, 2, 3
# trzecia wartość nie ma do czego być przypisana, powoduje błąd

# %%
X = 1, 2, 3 ; X[1] = 4
# brak nawiasów [] listy przy przypisaniu do X

# %%
X = [1, 2, 3] ; X[3] = 4
# listy numerowane są od 0, x[3] nie istnieje i przypisanie do niego spowoduje bład

# %%
X = "abc" ; X.append("d")
# .append działa dla list, X jest w formie ciągu znaków

# %%
L = list(map(pow, range(8)))
# funkcja pow() wymaga drugiego argumentu, który nie jest podany
