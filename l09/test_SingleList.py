from SingleList import SingleList, Node


def test_remove_tail():
    lst = SingleList()
    lst.insert_tail(Node(1))
    lst.insert_tail(Node(2))
    lst.insert_tail(Node(3))
    assert lst.remove_tail().data == 3
    assert lst.remove_tail().data == 2
    assert lst.remove_tail().data == 1
    assert lst.count() == 0


def test_join():
    lst = SingleList()
    lst.insert_tail(Node(1))
    lst.insert_tail(Node(2))
    lst.insert_tail(Node(3))
    lst2 = SingleList()
    lst2.insert_tail(Node(4))
    lst2.insert_tail(Node(5))
    lst2.insert_tail(Node(6))
    lst.join(lst2)
    assert lst2.count() == 0
    for i in range(1, 7):
        assert lst.remove_head().data == i


def test_clear():
    lst = SingleList()
    lst.insert_tail(Node(1))
    lst.insert_tail(Node(2))
    lst.clear()
    assert lst.head is None
    assert lst.tail is None
    assert lst.count() == 0
