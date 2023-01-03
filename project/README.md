# Generacja Labiryntu za pomocą Algorytmu Prima

Projekt zaliczeniowy na kurs języka Python.

## Opis projektu

Program tworzy graf, gdzie każdy wierzchołek ma przypisane koordynaty x i y na dwuwymiarowej siatce, połączony jest ze swoimi czterema sąsiadami, i którego krawędzie mają losowe wagi, a następnie znajduje drzewo rozpinające za pomocą algorytmu Prima.  
Następnie program wyświetla utworzony "labirynt", traktując krawędzie drzewa jako przejścia, a ich brak jako ściany. Wyświetlanie labiryntu jest zrealizowane za pomocą `tkinter.Canvas`, a sam interfejs graficzny oferuje dodatkowo możliwość dostosowania ilości wierzchołków grafu, a co za tym idzie złożoności labiryntu.  
Implementacja struktury grafu oraz algorytmu drzewa rozpinającego jest napisana własnoręcznie, w celu dostosowania jej do problemu, jedynie jako kolejka priorytetowa do algorytmu Prima została użyta gotowa struktura danych `queue.PriorityQueue`.

## Interfejs
![2023-01-03_1672748549 _python](https://user-images.githubusercontent.com/48099798/210359555-869e8a89-f72e-4bed-829e-9a91dc31ec79.png)

1. **Width** - pole tekstowe, przyjmujące liczbę naturalną. Ustala ilość pól składających się na jeden rząd labiryntu.
2. **Height** - pole tekstowe, przyjmujące liczbę naturalną. Ustala ilość pól składających się na jedną kolumnę labiryntu.
3. **Draw passages** - checkbox. W przypadku zaznaczenia, każde pole labiryntu rysuje w swoich otwartych przejściach krawędź o kolorze żółtym (zamiast nie rysowania w cale).
4. **Show tile numbers** - checkbox. W przypadku zaznaczenia, każde pole labiryntu wyświetla swój numer porządkowy.
5. **Draw** - przycisk. Rysuje labirynt na podstawie powyższych ustawień. Przy każdym naciśnięciu cały algorytm uruchamiany jest od nowa, co powoduje powstanie nowego losowego labiryntu.

## Algorytm prima

Zaimplementowany jest w metodzie `spanningTree` w implementacji grafu użytej do projektu.  
Algorytm tworzy z grafu tzw. "Drzewo rozpinające", tj. podzbiór grafu zawierający wszystkie jego wierzchołki oraz minimalną liczbę krawędzi potrzebną, aby graf był spójny.  
   
Otrzymane drzewo jest następnie wykorzystane do narysowania labiryntu, gdzie każdy wierzchołek jest traktowany jako pole, krawędź między wierzchołkami jako przejście między polami, a brak krawędzi jako ściana między polami.  
   
Algorytm zaczyna od dodania jednego wierzchołka do drzewa.  
Następnie wszystkie krawędzie tego wierzchołka dodawane są do kolejki priorytetowej, z której będą wyciągane na podstawie swoich wag (losowo przypisanych przy tworzeniu grafu).  
Następnie, dopóki wszystkie wierzchołki nie trafią do grafu, wyciągana jest pierwsza krawędź z kolejki i jeśli wierzchołek, do którego prowadzi, nie należy do drzewa, to jest on dodawany do drzewa, a jego krawędzie do kolejki, a jeśli wierzchołek już został dodany do drzewa, to wyciągana jest kolejna krawędź z kolejki.
