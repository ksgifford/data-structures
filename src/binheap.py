"""Defines data structure for implementing a binary heap."""
# -*- coding: utf-8 -*-
import math


class BinHeap(object):
    """Class for implementing a binary heap."""

    def __init__(self, seq=None):
        if not seq:
            self._heap_list = []
        else:
            self._heap_list = list(seq)
            self._max_heapify()

    def _max_heapify(self):
        idx = 0

        while idx < len(self._heap_list):
            left_val = _child_left()
            right_val = _child_right()
            parent_val = self._heap_list[idx]

            # _child functions should return indexes, not values?
            if self.compare_max(left_val, parent_val):
                self._swap()
            idx -= 1

    def _swap(self, child_idx, parent_idx):
        heap = self._heap_list
        heap[child_idx], heap[parent_idx] = heap[parent_idx], heap[child_idx]

    def _compare_max(child, parent):
        return child > parent

    def _parent(self, idx):
        if idx == 0:
            return None
        else:
            return self._heap_list[math.floor((idx - 1) / 2)]

    def _child_left(self, idx):
        try:
            return self._heap_list[2 * idx + 1]
        except IndexError:
            return None

    def _child_right(self, idx):
        try:
            return self._heap_list[2 * idx + 2]
        except IndexError:
            return None

    def insert(self, val):
        pass

    def extract(self):
        pass
