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
        if new_next:
            new_next.prev_node = self

    def set_prev(self, new_prev):
        """Set the node's previous reference to provide node."""
        self.prev_node = new_prev
        if new_prev:
            new_prev.next_node = self


class DblLinkedList(object):
    """Establish class for linked list and associated functions."""

    def __init__(self, seq=None):
        """Initialize linked list and set head."""
        cur_node = None
        prev_node = None
        self.head = None
        self.tail = None

        for val in seq or []:
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
        if not self.tail:
            self.tail = new_node
        self.head = new_node

    def append(self, val):
        """Add node to tail of linked list and update previous reference."""
        new_node = Node(val)
        new_node.set_prev(self.tail)
        if not self.head:
            self.head = new_node
        self.tail = new_node

    def pop(self):
        """Remove the first node from the head and return its value."""
        if not self.head:
            raise IndexError("Cannot pop from empty list.")
        else:
            popped_node = self.head
            self.head = self.head.next_node
            if self.head:
                self.head.prev_node = None
            else:
                self.tail = None
            return popped_node.val

    def shift(self):
        """Remove node from tail and return its value."""
        if not self.tail:
            raise IndexError("Cannot shift from empty list.")
        else:
            shifted_node = self.tail
            self.tail = self.tail.prev_node
            if self.tail:
                self.tail.next_node = None
            else:
                self.head = None
            return shifted_node.val

    def remove(self, val):
        """Search list for value and remove first instance."""
        search_node = self.head

        while search_node:
            if search_node.val == val:
                if search_node == self.head:
                    self.pop()
                    break
                elif search_node == self.tail:
                    self.shift()
                    break
                else:
                    search_node.prev_node.set_next(search_node.next_node)
                    break
            else:
                search_node = search_node.next_node
        else:
            raise ValueError("Search value not found.")
