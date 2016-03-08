"""Defines data structure for implementing linked list."""
# -*- coding: utf-8 -*-


class Linked_List(object):
    """Establish class to contain linked list methods."""

    def __init__(self, seq=None):
        """Construct linked list from optional sequence."""
        if not seq:
            self.head = ()
        else:
            node = None
            for idx, item in enumerate(seq):
                node = (item, node)
                if idx == len(seq) - 1:
                    self.head = node

    def insert(self, val):
        """Insert new value into list and set head at new value."""
        self.head = (val, self.head)

    def pop(self):
        """Return value at head and remove it from the list."""
        if not self.head:
            return None
        val = self.head[0]
        self.head = self.head[1]
        return val

    def size(self, node=None):
        """Return size of list by recursively traversing it."""
        if node is None:
            node = self.head
        if not self.head:
            return 0
        if node[1] is None:
            return 1
        else:
            return self.size(node[1]) + 1

    def search(self, val, node=False):
        """Return node containg the given value or None if not found."""
        if node is False:
            node = self.head
        if not node:
            return None
        if node[0] == val:
            return node
        else:
            return self.search(val, node[1])

    def remove(self, node_rm, cur_node=False):
        """Remove given node from list in place."""
        if not node_rm:
            return None
        if cur_node is False:
            self.head = self.remove(node_rm, self.head)
        elif cur_node is None:
            return None
        elif cur_node == node_rm:
            return cur_node[1]
        else:
            return (cur_node[0], self.remove(node_rm, cur_node[1]))

    def display(self, node=False):
        """Print the list as a tuple literal."""
        if node is False:
            node = self.head
        if not node:
            return ()
        else:
            return (node[0],) + self.display(node[1])
