"""Defines data structure for implementing a priority queue."""
# -*- coding: utf-8 -*-
from binheap import BinHeap


class PriorityQ(object):
    """Class for implementing a priority queue."""

    def __init__(self):
        self._heap = BinHeap(order='min')
        self._cumulative_idx = 0

    def insert(self, pri, val):
        self._heap.push((pri, self._cumulative_idx, val))
        self._cumulative_idx += 1

    def pop(self):
        result = self._heap.pop()
        return result[2]

    def peek(self):
        return self._heap._heap_list[0]
