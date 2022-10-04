# Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?

#-------------------------------------
# %%
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
# podany kod jest poprawny, mimo kilku niepotrzebnych średników

#-------------------------------------
# %%
for i in "axby": if ord(i) < 100: print (i)
# podany kod jest niepoprawny, wiele ekspresji w jednej linijce powoduje bład

#-------------------------------------
# %%
for i in "axby": print (ord(i) if ord(i) < 100 else i)
# podany kod jest poprawny
# %%
