# Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący x oraz trzecią potęgę x.
# Zatrzymanie programu następuje po wpisaniu z klawiatury stop.
# Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.

while True:
    rawX = input('Podaj liczbe rzeczywista:\n')
    if rawX == 'stop':
        break
    try:
        x = float(rawX)
    except ValueError:
        print('Podano napis zamiast liczby')
        continue

    print(x)
    print(x**3)
