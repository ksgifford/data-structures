"""Unit tests for d_graph.py module."""
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(scope='function')
def instance():
    from d_graph import DGraph
    test_graph = DGraph()
    test_graph.add_node('A')
    test_graph.add_node('B')
    test_graph.add_node('C')
    test_graph.add_node('D')
    test_graph.add_edge('A', 'B')
    test_graph.add_edge('A', 'D')
    test_graph.add_edge('A', 'C')
    test_graph.add_edge('B', 'C')
    return test_graph


def test_nodes(instance):
    assert sorted(instance.nodes()) == ['A', 'B', 'C', 'D']


def test_edges(instance):
    expected = ['A>B', 'A>C', 'A>D', 'B>C']
    assert sorted(instance.edges()) == sorted(expected)


def test_add_nodes(instance):
    instance.add_node('E')
    assert sorted(instance.nodes()) == ['A', 'B', 'C', 'D', 'E']


def test_add_edge(instance):
    instance.add_edge('C', 'D')
    expected = ['A>B', 'A>C', 'A>D', 'B>C', 'C>D']
    assert sorted(instance.edges()) == sorted(expected)


def test_del_node(instance):
    instance.del_node('B')
    expected_edges = ['A>C', 'A>D']
    expected_nodes = ['A', 'C', 'D']
    assert sorted(instance.edges()) == sorted(expected_edges)
    assert sorted(instance.nodes()) == sorted(expected_nodes)


def test_del_node_error(instance):
    with pytest.raises(KeyError):
        instance.del_node('Z')


def test_del_edge(instance):
    instance.del_edge('A', 'C')
    expected = ['A>B', 'A>D', 'B>C']
    assert sorted(instance.edges()) == sorted(expected)


def test_del_edge_error(instance):
    with pytest.raises(KeyError):
        instance.del_edge('B', 'D')


def test_has_node_true(instance):
    assert instance.has_node('A') is True


def test_has_node_false(instance):
    assert instance.has_node('Z') is False


def test_neighbors(instance):
    neighbors = instance.neighbors('A')
    assert sorted(neighbors) == sorted(['B', 'C', 'D'])


def test_neighbors_error(instance):
    with pytest.raises(KeyError):
        instance.neighbors('M')


def test_adjacent_true(instance):
    assert instance.adjacent('B', 'C') is True


def test_adjacent_false(instance):
    assert instance.adjacent('B', 'D') is False


def test_adjacent_error(instance):
    with pytest.raises(KeyError):
        instance.adjacent('B', 'Q')
