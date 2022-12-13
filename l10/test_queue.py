from queue import Queue
import pytest


def test_queue():
    q = Queue(5)

    assert q.is_empty() == True
    assert q.is_full() == False

    with pytest.raises(ValueError):
        q.get()

    q.put(1)
    q.put(2)
    q.put(3)
    
    assert q.is_empty() == False
    assert q.is_full() == False
    
    q.put(4)
    q.put(5)

    assert q.is_empty() == False
    assert q.is_full() == True

    with pytest.raises(ValueError):
        q.put(6)

    assert q.get() == 1
    assert q.get() == 2
    
    assert q.is_full() == False
    
    q.put(6)
    q.put(7)
    
    assert q.is_full() == True

    with pytest.raises(ValueError):
        q.put(6)
