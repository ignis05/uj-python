# Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.

value = int(input('Podaj n: '))


def fibonacci(n):
    a = 0
    b = 1
    for _ in range(0, n):
        a, b = b, a + b
    return a
  
print(fibonacci(value))
