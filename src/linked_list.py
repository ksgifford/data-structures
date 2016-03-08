# -*- coding: utf-8 -*-


class Linked_List(object):

    def __init__(self, seq=None):
        if seq is None or not seq:
            self.head = ()
        else:
            node = None
            for idx, item in enumerate(seq):
                node = (item, node)
                if idx == len(seq) - 1:
                    self.head = node

    def insert(self, val):
        self.head = (val, self.head)

    def pop(self):
        if not self.head:
            return None
        val = self.head[0]
        self.head = self.head[1]
        return val

    def size(self, node=None):
        if node is None:
            node = self.head
        if not self.head:
            return 0
        if node[1] is None:
            return 1
        else:
            return self.size(node[1]) + 1

    def search(val):
        pass

    def remove(node):
        pass

    def display(self, node=None):
        if node is None:
            node = self.head
        if node[1] is None:
            return (node[0],)
        else:
            return (node[0],) + self.display(node[1])
