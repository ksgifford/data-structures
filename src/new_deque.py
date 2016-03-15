"""Defines data structure for implementing a deque."""
# -*- coding: utf-8 -*-
from dbl_linked_list import DblLinkedList


class Deque(object):
    """Establish class for deque. Methods composed from dbl_linked_list."""

    def __init__(self, seq=None):
        """Initialize deque."""
        self._deque = DblLinkedList(seq)

    def append(self, val):
        """Append value to end of deque."""
        self._deque.append(val)

    def appendleft(self, val):
        """Append value to front of deque."""
        self._deque.insert(val)

    def pop(self):
        """Remove last item from deque and return its value."""
        try:
            return self._deque.shift()
        except IndexError:
            raise IndexError("Cannot pop from end of an empty deque.")

    def popleft(self):
        """Remove first item from deque and return its value."""
        try:
            return self._deque.pop()
        except IndexError:
            raise IndexError("Cannot pop from head of an empty deque.")

    def peek(self):
        """Return value of last item in deque."""
        try:
            return self._deque.tail.val
        except AttributeError:
            return None

    def peekleft(self):
        """Return value of first item in deque."""
        try:
            return self._deque.head.val
        except AttributeError:
            return None

    def size(self):
        """Calculate number of items in the deque and return it."""
        cur_node = self._deque.head
        counter = 0
        while cur_node:
            counter += 1
            cur_node = cur_node.next_node
        return counter
