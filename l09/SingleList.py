class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        # return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(1)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    # ---- 9.1 ----

    def remove_tail(self):   # klasy O(n)
        # Zwraca cały węzeł, skraca listę.
        # Dla pustej listy rzuca wyjątek ValueError.
        res = self.tail
        if self.length == 0:
            raise ValueError('list is empty')
        elif self.length == 1:
            self.head = self.tail = None
            self.length -= 1
            return res

        node = self.head
        while (node.next != self.tail):
            node = node.next

        self.length -= 1
        node.next = None
        self.tail = node
        return res

    def join(self, other):   # klasy O(1)
        # Węzły z listy other są przepinane do listy self na jej koniec.
        # Po zakończeniu operacji lista other ma być pusta.
        self.tail.next = other.head
        self.tail = other.tail
        self.length += other.length
        other.clear()

    def clear(self):     # czyszczenie listy
        self.head = self.tail = None
        self.length = 0

    # ---- 9.2 ----

    def search(self, data):   # klasy O(n)
        # Zwraca łącze do węzła o podanym kluczu lub None.
        if self.length == 0:
            return None
        node = self.head
        while (node.data != data):
            if node.next:
                node = node.next
            else:
                return None
        return node

    def find_min(self):   # klasy O(n)
        # Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy.
        if self.length == 0:
            return None
        minVal = self.head.data
        minNode = self.head
        node = self.head
        while (node is not None):
            if (node.data < minVal):
                minVal = node.data
                minNode = node
            node = node.next
        return minNode

    def find_max(self):   # klasy O(n)
        # Zwraca łącze do węzła z największym kluczem lub None dla pustej listy.
        if self.length == 0:
            return None
        maxVal = self.head.data
        maxNode = self.head
        node = self.head
        while (node is not None):
            if (node.data > maxVal):
                maxVal = node.data
                maxNode = node
            node = node.next
        return maxNode

    def reverse(self):   # klasy O(n)
        # Odwracanie kolejności węzłów na liście.
        if self.length <= 1:
            return

        self.tail = self.head
        prevNode = None
        node = self.head
        while (node is not None):
            next = node.next
            node.next = prevNode
            prevNode = node
            node = next
        self.head = prevNode
