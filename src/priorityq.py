"""Defines data structure for implementing a priority queue."""
# -*- coding: utf-8 -*-
from binheap import BinHeap


class PriorityQ(object):
    """Class for implementing a priority queue."""

    def __init__(self):
        self._heap = BinHeap(order='min')
        self._cumulative_idx = 0

    def insert(self, pri, val):
        """Insert a value at the end of the priority queue."""
        self._heap.push((pri, self._cumulative_idx, val))
        self._cumulative_idx += 1

    def pop(self):
        """Remove and return the value at the root of the priority queue."""
        try:
            result = self._heap.pop()
            return result[2]
        except IndexError:
            raise IndexError("Cannot pop from empty queue.")

    def peek(self):
        """Return the value of at the root of the priority queue."""
        try:
            return self._heap._heap_list[0][2]
        except IndexError:
            return None
