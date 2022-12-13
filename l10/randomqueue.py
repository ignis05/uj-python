# 10.8
# Stworzyć ADT w postaci kolejki losowej, z której elementy będą pobierane w losowej kolejności.
# Zadbać o to, aby każda operacja była wykonywana w stałym czasie, niezależnie od liczby elementów w kolejce.

import random


class RandomQueue:

    def __init__(self, maxSize=10):
        self.q = [None] * maxSize
        self.maxSize = maxSize
        self.size = 0

    @property
    def lastindex(self):
        return self.size - 1

    def insert(self, item):   # wstawia element w czasie O(1)
        if self.is_full():
            raise ValueError('Queue is full')

        self.q[self.size] = item
        self.size += 1

    def remove(self):   # zwraca losowy element w czasie O(1)
        if self.is_empty():
            raise ValueError('Queue is empty')

        # get random index
        i = random.randint(0, self.lastindex)
        item = self.q[i]

        # if it's last index, then just remove it
        if i == self.lastindex:
            self.q[i] = None
        # else, replace it with last element and remove the last element
        else:
            self.q[i] = self.q[self.lastindex]
            self.q[self.lastindex] = None

        self.size -= 1
        return item

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.maxSize

    def clear(self):   # czyszczenie listy
        self.q = [None] * self.maxSize
        self.size = 0
