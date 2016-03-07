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

    def insert(val):
        pass

    def pop():
        pass

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
            return self.display(node[1]) + (node[0],)
