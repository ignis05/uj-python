from queue import Queue
import pytest


def test_queue():
    q = Queue(5)

    with pytest.raises(ValueError):
        q.get()

    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    q.put(5)

    with pytest.raises(ValueError):
        q.put(6)

    assert q.get() == 1
    assert q.get() == 2
    q.put(6)
    q.put(7)

    with pytest.raises(ValueError):
        q.put(6)
