"""Unit tests for binheap.py module."""
# -*- coding: utf-8 -*-
import pytest


TEST_CASES = [
    ((2, 10, 14, 8), [14, 10, 2, 8]),
    ((3, 19, 47, 1, 0, 35, -1, -10), [47, 19, 35, 1, 0, 3, -1, -10]),
    ((10, 14, 15, 17, 18, 19, 20, 30), [])
]

TESTS = [
    (1, 2, 3, 4),
    [4, 3, 9, 1],
    [1],
]


@pytest.mark.parametrize('seq', TESTS)
def test_init(seq):
    """Test that BinHeap properly constructs from given sequence."""
    from binheap import BinHeap
    heap = BinHeap(seq)
    assert heap._heap_list == list(reversed(sorted(list(seq))))


@pytest.mark.parametrize('seq', TESTS)
def test_pop_result(seq):
    """Test result of BinHeap's pop method."""
    from binheap import BinHeap
    heap = BinHeap(seq)
    assert heap.pop() == max(seq)


@pytest.mark.parametrize('seq', TESTS)
def test_pop_len(seq):
    """Test length of BinHeap's internal list after pop."""
    from binheap import BinHeap
    heap = BinHeap(seq)
    heap.pop()
    assert len(heap._heap_list) == len(seq) - 1


@pytest.mark.parametrize('seq', TESTS)
def test_push_len(seq):
    """Test length of BinHeap's internal list after push."""
    from binheap import BinHeap
    heap = BinHeap(seq)
    heap.push(0)
    assert len(heap._heap_list) == len(seq) + 1
