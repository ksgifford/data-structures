"""Defines data structure for implementing a queue."""
# -*- coding: utf-8 -*-
from dbl_linked_list import DblLinkedList


class Queue(object):
    """Establish class for Queue. Methods composed from DblLinkedList class."""

    def __init__(self, seq):
        """Initialize Queue, based on Double Linked List constructor."""
        self._queue = DblLinkedList(seq)

    def enqueue(self, val):
        """Add val to end of the queue."""
        self._queue.append(val)

    def dequeue(self):
        """Remove and return first item in queue."""
        try:
            return self._queue.pop()
        except IndexError:
            print("IndexError caught from DBLL")
            raise IndexError("Queue is empty.")

    def peek(self):
        """Return value of the first object in the queue."""
        if self._queue.head:
            return self._queue.head.val
        else:
            return None

    def size(self):
        """Loop through the queue and count the number of items."""
        cur_node = self._queue.head
        count = 0

        while cur_node:
            cur_node = cur_node.next_node
            count += 1

        return count
