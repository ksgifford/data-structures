"""Defines data structure for implementing a doubly linked list."""
# -*- coding: utf-8 -*-


class Node(object):
    """Establish node structure for storing data and pointers in list."""

    def __init__(self, val=None, next_node=None, prev_node=None):
        """Construct node instance."""
        self.val = val
        self.next_node = next_node
        self.prev_node = prev_node

    def get_val(self):
        """Return the data portion of the node."""
        return self.val

    def get_next(self):
        """Return reference to the next node in the list."""
        return self.next_node

    def get_prev(self):
        """Return reference to previous node in the list."""
        return self.prev_node

    def set_next(self, new_next):
        """Set the node's next reference to provided node."""
        self.next_node = new_next
        new_next.prev_node = self

    def set_prev(self, new_prev):
        """Set the node's previous reference to provide node."""
        self.prev_node = new_prev
        new_prev.next_node = self


class DblLinkedList(object):
    """Establish class for linked list and associated functions."""

    def __init__(self, seq=None):
        """Initialize linked list and set head."""
        cur_node = None
        prev_node = None
        self.head = None
        self.tail = None

        for val in seq:
            cur_node = Node(val, prev_node=prev_node)
            if prev_node:
                prev_node.next_node = cur_node
            if not self.head:
                self.head = cur_node
            prev_node = cur_node
        if cur_node:
            self.tail = cur_node

    def insert(self, val):
        """Add node to linked list and update next and previous references."""
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node

    def append(self, val):
        """Add node to tail of linked list and update previous reference."""
        new_node = Node(val)
        new_node.set_prev(self.tail)
        self.tail = new_node

    def pop(self):
        """Remove the first value from the head and return it."""
        popped_node = self.head
        self.head = self.head.next_node
        self.head.prev_node = None
        return popped_node.val

    def shift(self):
        pass

    def remove(self, val):
        pass
