"""Unit tests for priorityq.py module."""
# -*- coding: utf-8 -*-
import pytest
import math


TESTS = [
    None,
    (),
    [],
    '',
    'a',
    (1,),
    [1],
    'abc',
    (1, 2, 3, 4),
    [4, 3, 9, 1],
    'jdslajdlfkjaldgna',
    tuple(range(10000)),
    list(range(10000)),
    'kliijj;lkijgasdfanfiiofi48ghgknlvili;wgr;w',
]


# def test_pop_result(instance_and_seq):
#     """Test result of BinHeap's pop method."""
#     instance, seq = instance_and_seq
#     if seq:
#         assert instance.pop() == max(seq)
#
#
# def test_pop_len(instance_and_seq):
#     """Test length of BinHeap's internal list after pop."""
#     instance, seq = instance_and_seq
#     if seq:
#         instance.pop()
#         assert len(instance._heap_list) == len(seq) - 1
#
#
def test_pop_empty(instance_and_seq):
    """Test that popping an empty list raises an index error."""
    instance, seq = instance_and_seq
    if not seq:
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
