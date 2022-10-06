# Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

def factorial(n):
  result = 1
  for i in range(1,n+1):
    result *= i
  return result


print(factorial(5))
print(factorial(1))
print(factorial(0))