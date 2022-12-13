# 10.4
# Poprawić metodę get(), aby w przypadku pustej kolejki zwracała wyjątek.
# Poprawić metodę put() w tablicowej implementacji kolejki, aby w przypadku przepełnienia kolejki zwracała wyjątek.
# Napisać kod testujący kolejkę.

class Queue:
    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0           # pierwszy do pobrania
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.tail + 1) % self.n == self.head

    def put(self, data):
        if (self.tail + 1) % self.n == self.head:
            raise ValueError("Queue is full")

        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.head == self.tail:
            raise ValueError("Queue is empty")

        data = self.items[self.head]
        self.items[self.head] = None   # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data
