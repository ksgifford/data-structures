# -*- coding: utf-8 -*-


class Linked_List(object):

    def __init__(self, seq=None):
        if seq is None:
            self.seq = []
        else:
            self.seq = seq
            node = None
            for idx, item in enumerate(seq):
                node = (item, node)
                if idx == len(seq) - 1:
                    self.head = node

    def insert(val):
        pass

    def pop():
        pass

    def size():
        pass

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
