"""Defines data structure for implementing a binary heap."""
# -*- coding: utf-8 -*-
import math


class BinHeap(object):
    """Class for implementing a binary heap."""

    def __init__(self, seq=None):
        """Construct new BinHeap instance."""
        if not seq:
            self._heap_list = []
        else:
            self._heap_list = list(seq)
            self._build_heap()

    def _build_heap(self):
        idx = len(self._heap_list) - 1
        while idx >= 0:
            self._max_heapify(idx)
            idx -= 1

    def _max_heapify(self, parent_idx):
        left = self._child_left(parent_idx)
        right = self._child_right(parent_idx)

        if self._compare_max(left, parent_idx):
            largest = left
        else:
            largest = parent_idx

        if self._compare_max(right, largest):
            largest = right

        if largest != parent_idx:
            self._swap(largest, parent_idx)
            self._max_heapify(largest)

    def _swap(self, idx1, idx2):
        heap = self._heap_list
        heap[idx1], heap[idx2] = heap[idx2], heap[idx1]

    def _compare_max(self, child_idx, parent_idx):
        try:
            return self._heap_list[child_idx] > self._heap_list[parent_idx]
        except IndexError:
            return False

    def _parent(self, idx):
        if idx == 0:
            return None
        else:
            return self._heap_list[math.floor((idx - 1) / 2)]

    def _child_left(self, idx):
        return 2 * idx + 1

    def _child_right(self, idx):
        return 2 * idx + 2

    def push(self, val):
        """Append value to end of heap and re-sort to heap specification."""
        self._heap_list.append(val)
        self._build_heap()

    def pop(self):
        """Remove the root value of the heap, then re-sort it."""
        try:
            result = self._heap_list.pop(0)
        except IndexError:
            raise IndexError("Cannot pop from an empty heap.")
        self._build_heap()
        return result
