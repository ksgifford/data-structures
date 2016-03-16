"""Unit tests for binheap.py module."""
# -*- coding: utf-8 -*-
import pytest
import math

TEST_CASES = [
    ((2, 10, 14, 8), [14, 10, 2, 8]),
    ((3, 19, 47, 1, 0, 35, -1, -10), [47, 19, 35, 1, 0, 3, -1, -10]),
    ((10, 14, 15, 17, 18, 19, 20, 30), [])
]

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


@pytest.fixture(scope='function', params=TESTS)
def instance_and_seq(request):
    from binheap import BinHeap
    seq = request.param
    if seq is None:
        instance = BinHeap()
        seq = []
    else:
        instance = BinHeap(seq)

    return (instance, seq)


def _is_real_heap(heap, parent_idx):
    for child_idx, child_val in enumerate(heap):

        parent_idx = max([0, math.floor((child_idx - 1) / 2)])

        if child_val > heap[parent_idx]:
            return False
    return True


def test_init(instance_and_seq):
    """Test that BinHeap properly constructs from given sequence."""
    instance, seq = instance_and_seq
    assert is_real_heap(instance._heap_list, 0)


def test_pop_result(instance_and_seq):
    """Test result of BinHeap's pop method."""
    instance, seq = instance_and_seq
    if seq:
        assert instance.pop() == max(seq)


def test_pop_len(instance_and_seq):
    """Test length of BinHeap's internal list after pop."""
    instance, seq = instance_and_seq
    if seq:
        instance.pop()
        assert len(instance._heap_list) == len(seq) - 1


def test_pop_empty(instance_and_seq):
    """Test that popping an empty list raises an index error."""
    instance, seq = instance_and_seq
    if not seq:
        with pytest.raises(IndexError):
            instance.pop()


def test_push_len(instance_and_seq):
    """Test length of BinHeap's internal list after push."""
    instance, seq = instance_and_seq
    if isinstance(seq, str):
        instance.push('a')
    else:
        instance.push(0)
    assert len(instance._heap_list) == len(seq) + 1
