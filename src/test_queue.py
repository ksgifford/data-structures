"""Unit tests for queue.py module."""
# -*- coding: utf-8 -*-
import pytest


TEST_INIT = [
    ([1, 2, 3, 4]),
    ('abcd'),
    (()),
]


TEST_ENQUEUE = [
    ([1, 2, 3], 4, [1, 2, 3, 4]),
    ('abc', 'x', ['a', 'b', 'c', 'x']),
    ([], 'A', ['A']),
]


TEST_DEQUEUE = [
    ([1, 2, 3, 4], 1),
    ('abcd', 'a'),
    ([], IndexError),
]


TEST_PEEK = [
    ([1, 2, 3, 4], 1),
    ('abcd', 'a'),
    ([], None),
]


TEST_SIZE = [
    ([1, 2, 3], 3),
    ('abcde', 5),
    (range(50), 50),
    ([], 0),
]


def display_q(queue):
    """Return a list showing given queue, which has no display method."""
    cur_node = queue._queue.head
    display_lst = []
    while cur_node:
        display_lst.append(cur_node.val)
        cur_node = cur_node.next_node
    return display_lst


@pytest.mark.parametrize('seq', TEST_INIT)
def test_init(seq):
    """Test class constructor of Queue."""
    from new_queue import Queue
    instance = Queue(seq)
    assert isinstance(instance, Queue)


@pytest.mark.parametrize('seq, val, new_q', TEST_ENQUEUE)
def test_enqueue(seq, val, new_q):
    """Test the enqueue method."""
    from new_queue import Queue
    test_q = Queue(seq)
    test_q.enqueue(val)
    assert display_q(test_q) == new_q


@pytest.mark.parametrize('seq, expected', TEST_DEQUEUE)
def test_dequeue(seq, expected):
    """Test the dequeue method."""
    from new_queue import Queue
    test_q = Queue(seq)
    if not seq:
        with pytest.raises(IndexError):
            return_val = test_q.dequeue()
    else:
        return_val = test_q.dequeue()
        assert return_val == expected


@pytest.mark.parametrize('seq, expected', TEST_PEEK)
def test_peek(seq, expected):
    """Test the peek method."""
    from new_queue import Queue
    test_q = Queue(seq)
    assert test_q.peek() == expected


@pytest.mark.parametrize('seq, size', TEST_SIZE)
def test_size(seq, size):
    """Test the size method."""
    from new_queue import Queue
    test_q = Queue(seq)
    assert test_q.size() == size
