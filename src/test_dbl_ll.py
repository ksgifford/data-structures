"""Unit tests for dbl_linked_list.py module."""
# -*- coding: utf-8 -*-
import pytest


TEST_LST = [
    ([1, 2, 3], 1, 2, 3),
    ('abc', 'a', 'b', 'c'),
    (range(100), 0, 1, 99),
]


TEST_INSERT = [
    ([1, 2, 3], 5, 5, 1, 3),
    ('abc', 'x', 'x', 'a', 'c'),
    (range(100), 101, 101, 0, 99),
]


TEST_APPEND = [
    ([1, 2, 3], 5, 1, 5, 3),
    ('abc', 'x', 'a', 'x', 'c'),
    (range(100), 500, 0, 500, 99),
]


TEST_POP = [
    ([1, 2, 3], 1, 2),
    ('abc', 'a', 'b'),
    (range(100), 0, 1),
]


@pytest.mark.parametrize('seq, head_val, head_next_val, tail_val', TEST_LST)
def test_init(seq, head_val, head_next_val, tail_val):
    from dbl_linked_list import DblLinkedList
    test_list = DblLinkedList(seq)
    assert test_list.head.val == head_val
    assert test_list.head.next_node.val == head_next_val
    assert test_list.tail.val == tail_val


@pytest.mark.parametrize('seq, insert_val, head_val, head_next_val, tail_val', TEST_INSERT)
def test_insert(seq, insert_val, head_val, head_next_val, tail_val):
    from dbl_linked_list import DblLinkedList
    test_list = DblLinkedList(seq)
    test_list.insert(insert_val)
    assert test_list.head.val == head_val
    assert test_list.head.next_node.val == head_next_val
    assert test_list.tail.val == tail_val


@pytest.mark.parametrize('seq, append_val, head_val, tail_val, tail_prev_val', TEST_APPEND)
def test_append(seq, append_val, head_val, tail_val, tail_prev_val):
    from dbl_linked_list import DblLinkedList
    test_list = DblLinkedList(seq)
    test_list.append(append_val)
    assert test_list.head.val == head_val
    assert test_list.tail.val == tail_val
    assert test_list.tail.prev_node.val == tail_prev_val


@pytest.mark.parametrize('seq, popped_val, head_val', TEST_POP)
def test_pop(seq, popped_val, head_val):
    from dbl_linked_list import DblLinkedList
    test_list = DblLinkedList(seq)
    assert test_list.pop() == popped_val
    assert test_list.head.val == head_val
