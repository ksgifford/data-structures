"""Unit tests for priorityq.py module."""
# -*- coding: utf-8 -*-
import pytest


def test_peek():
    """Test that peeking reveals the root of the priority queue."""
    from priorityq import PriorityQ
    push_list = [(2, 'maintenance'),
                 (1, 'staff mtg'),
                 (1, 'stand-up'),
                 (0, 'server crash'),
                 (0, 'boss DUI')]

    test_q = PriorityQ()
    for pri, val in push_list:
        test_q.insert(pri, val)

    assert test_q.peek() == 'server crash'


def test_pop_empty():
    """Test that popping an empty list raises an index error."""
    from priorityq import PriorityQ
    instance = PriorityQ()

    with pytest.raises(IndexError):
        instance.pop()


def test_insert():
    from priorityq import PriorityQ
    push_list = [(2, 'maintenance'),
                 (1, 'staff mtg'),
                 (1, 'stand-up'),
                 (0, 'server crash')]

    pop_list = ['server crash', 'staff mtg', 'stand-up', 'maintenance']

    test_q = PriorityQ()
    for pri, val in push_list:
        test_q.insert(pri, val)

    for item in pop_list:
        assert test_q.pop() == item
