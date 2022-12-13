from randomqueue import RandomQueue
import pytest


def test_randomqueue():
    values = [1, 2, 3]

    q = RandomQueue(3)

    assert q.is_empty() == True
    assert q.is_full() == False

    with pytest.raises(ValueError):
        q.remove()

    q.insert(1)

    assert q.is_empty() == False
    assert q.is_full() == False

    q.insert(2)
    q.insert(3)

    assert q.is_empty() == False
    assert q.is_full() == True

    with pytest.raises(ValueError):
        q.insert(0)

    assert q.remove() in values
    assert q.remove() in values

    assert q.is_full() == False

    q.insert(10)

    if q.remove() == 10:
        assert q.remove() in values
    else:
        assert q.remove() == 10

    assert q.is_empty() == True

    with pytest.raises(ValueError):
        q.remove()
