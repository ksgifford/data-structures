"""Defines data structure for implementing linked list."""
# -*- coding: utf-8 -*-


class Node(object):
    """Establish node structure for storing data and pointers in list."""

    def __init__(self, val=None, next_node=None):
        """Construct node instance."""
        self.val = val
        self.next = next_node


class LinkedList(object):
    """Establish class for linked list and associated functions."""

    def __init__(self, seq=None):
        """Initialize linked list and set head."""
        self.head = None

        cur_node = None
        for val in seq or []:
            cur_node = Node(val, cur_node)
        if cur_node:
            self.head = cur_node

    def display(self):
        """Print the list as a tuple literal."""
        display_list = []
        cur_node = self.head
        while cur_node:
            display_list.append(cur_node.val)
            cur_node = cur_node.next
        return str(tuple(display_list))

    def size(self):
        """Return the size of the LinkedList as an integer."""
        cur_node = self.head
        counter = 0
        while cur_node:
            counter += 1
            cur_node = cur_node.next
        return counter

    def insert(self, val):
        """Add node to linked list and update next and previous references."""
        # condense this into 1 line
        self.head = Node(val, self.head)

    def pop(self):
        """Remove the first node from the head and return its value."""
        if not self.head:
            raise IndexError("Cannot pop from empty LinkedList.")
        popped_node = self.head
        self.head = popped_node.next
        return popped_node.val

    # TODO
    def search(self, search_val):
        """Return node containg the given value or None if not found."""
        search_node = self.head
        while search_node:
            if search_node.val == search_val:
                return search_node
            search_node = search_node.next
        return None

    # TODO
    def remove(self, node_to_remove):
        """Remove given node from list in place."""
        prev_node = None
        search_node = self.head
        while search_node:
            if search_node == node_to_remove:
                if prev_node:
                    prev_node.next = search_node.next
                return search_node
            prev_node = search_node
            search_node = search_node.next


# # old version
# class Linked_List(object):
#     """Establish class to contain linked list methods."""

#     def __init__(self, seq=None):
#         """Construct linked list from optional sequence."""
#         if not seq:
#             self.head = ()
#         else:
#             node = None
#             for idx, item in enumerate(seq):
#                 node = (item, node)
#                 if idx == len(seq) - 1:
#                     self.head = node

#     def insert(self, val):
#         """Insert new value into list and set head at new value."""
#         self.head = (val, self.head)

#     def pop(self):
#         """Return value at head and remove it from the list."""
#         if not self.head:
#             return None
#         val = self.head[0]
#         self.head = self.head[1]
#         return val

#     def size(self, node=None):
#         """Return size of list by recursively traversing it."""
#         if node is None:
#             node = self.head
#         if not self.head:
#             return 0
#         if node[1] is None:
#             return 1
#         else:
#             return self.size(node[1]) + 1

#     def search(self, val, node=False):
#         """Return node containg the given value or None if not found."""
#         if node is False:
#             node = self.head
#         if not node:
#             return None
#         if node[0] == val:
#             return node
#         else:
#             return self.search(val, node[1])

#     def remove(self, node_rm, cur_node=False):
#         """Remove given node from list in place."""
#         if not node_rm:
#             return None
#         if cur_node is False:
#             self.head = self.remove(node_rm, self.head)
#         elif cur_node is None:
#             return None
#         elif cur_node == node_rm:
#             return cur_node[1]
#         else:
#             return (cur_node[0], self.remove(node_rm, cur_node[1]))

#     def display(self, node=False):
#         """Print the list as a tuple literal."""
#         if node is False:
#             node = self.head
#         if not node:
#             return ()
#         else:
#             return (node[0],) + self.display(node[1])
