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
