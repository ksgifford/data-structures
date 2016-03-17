"""Defines data structure for implementing simple directed graph structure."""
# -*- coding: utf-8 -*-


class D_Graph(object):
    """Class for implementing our direted graph structure."""
    def __init__(self):
        self._d_graph = {}

    def nodes(self):
        return self._d_graph.keys()

    def edges(self):
        edge_list = []
        for key, val in self._d_graph.items():
            for node in val:
                edge_list.append('>'.join(key, node))
        return edge_list

    def add_nodes(self, node):
        self._d_graph[node] = set()

    def add_edge(self, node1, node2):
        self._d_graph.setdefault(node1, set()).add(node2)
        self._d_graph.setdefault(node2, set())

    def del_node(self, node):
        try:
            del self._d_graph[node]
            for k, v in self._d_graph.items():
                try:
                    v.remove(node)
                except KeyError:
                    pass
        except KeyError:
            raise KeyError("Node not found in graph.")

    def del_edge(self, node1, node2):
        try:
            self._d_graph[node1].remove(node2)
        except KeyError:
            raise KeyError("Edge does not exist from {n1} to {n2}."
                           "".format(n1=node1, n2=node2))

    def has_node(self, node):
        return node in self._d_graph

    def neighbors(self, node):
        try:
            return list(self._d_graph[node])
        except KeyError:
            raise KeyError("{} is not a node in the graph.".format(node))

    def adjacent(self, node1, node2):
        try:
            self._d_graph[node2]
        except KeyError:
            raise KeyError("{} does not exist.".format(node2))
        try:
            return node2 in self._d_graph[node1]
        except KeyError:
            raise KeyError("{} does not exist.".format(node1))
