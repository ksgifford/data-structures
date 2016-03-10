"""Unit tests for linked_list.py module."""
# -*- coding: utf-8 -*-
import pytest
from collections import defaultdict, ordereddict
from linked_list import Node, LinkedList

TEST_NULL = 'TEST_NULL'

TEST_PARAMS = [
    'type',
    'instance',
    'popped_val',
    'display',
    'search_result',
    'size',

]

TEST_SEQUENCES = [
    None,  # case where we construct LinkedList without passing a sequence
    'this is a much longer string sequence of characters',
    range(100, 1000),
    tuple(range(100, 1000)),
    'abc',
    [1, 2, 3],
    (1, 2, 3),
    'x',
    [0],
    (8,),
    '',
    [],
    (),
]


@pytest.fixture(scope=function)
def make_instance(seq=None):
    if seq is not None:
        return LinkedList(seq)
    return LinkedList()


@pytest.fixture(scope=function)
def assemble_tuple(seq, **kwargs):
    dic = {}  # default to TEST_NULL
    dic['instance'] = make_instance(LinkedList)
    try:
        dic['popped_val'] = seq[0]
    except IndexError:
        dic['pop_error'] = IndexError
    return tuple([dic[param] for param in TEST_PARAMS])

{
    'instance': LinkedList,
    'popped_val': None,
    ''
}

TEST_LISTS = {
    'init': init_
}

@pytest.fixture
def instances():
    return



@pytest.fixture
def assemble_table(testname):
    table = [
        assemble_tuple(seq, **kwargs) for kwargs in ref_dict['testname']
    ]
    return


TEST_LST = [
    ([1, 2, 3], (3, 2, 1)),
    ('abc', ('c', 'b', 'a')),
    ([7, 8, 9], (9, 8, 7)),
    (range(100), tuple(reversed(range(100)))),
]

SEARCH_TEST = [
    ([1, 2, 3], 2, (2, (1, None))),
    ('abc', 'a', ('a', None)),
    ([7, 8, 9], 10, None),
    ([], 1, None)
]

SIZE_TEST = [
    ([0, 1, 2], 3),
    ([], 0),
    ('abcdefg', 7),
    ((0, 0, 'astring', 8, []), 5),
    (range(100), 100),
]

INSERT_TEST = [
    ([0, 1, 2], 'a'),
    ('abcdefg', 1),
    ((0, 0, 'astring', 8, []), 0),
    ([], []),
]

POP_TEST = [
    ([0, 1, 2], 2, 1),
    ([], None, None),
    ('abcdefg', 'g', 'f'),
    ((0, 0, 'astring', 8, []), [], 8),
    (range(100), 99, 98),
]

REMOVE_TEST = [
    ([1, 2, 3, 4], 3, (4, 2, 1)),
    ('abcd', 'a', ('d', 'c', 'b')),
    ([7, 8, 9], 9, (8, 7)),
    ([1, 2, 3, 4], 5, (4, 3, 2, 1)),
    ([], 'X', ())
]


@pytest.mark.parametrize('seq, result', TEST_LST)
def test_init(seq, result):
    """Test list constructor function with optional iterable."""
    from linked_list import Linked_List
    instance = LinkedList(seq)
    assert isinstance(object, class_or_type_or_tuple)


@pytest.mark.parametrize('seq, result', TEST_LST)
def test_display(seq, result):
    """Test display function against sample outputs."""
    from linked_list import LinkedList
    instance = LinkedList(seq)
    assert instance.display() == result


@pytest.mark.parametrize('seq, val', INSERT_TEST)
def test_insert(seq, val):
    """Test insert method to add value to list."""
    from linked_list import LinkedList
    instance = LinkedList(seq)
    instance.insert(val)
    assert instance.head[0] == val


@pytest.mark.parametrize('seq, popped_val, new_head', POP_TEST)
def test_pop(seq, popped_val, new_head):
    """Test pop method to remove value from head of list."""
    from linked_list import LinkedList
    instance = LinkedList(seq)
    assert instance.pop() == popped_val
    assert instance.size() == max([len(seq) - 1, 0])


@pytest.mark.parametrize('seq, val, result', SEARCH_TEST)
def test_search(seq, val, result):
    """Test search method for finding a given value in the list."""
    from linked_list import LinkedList
    instance = LinkedList(seq)
    assert instance.search(val) == result


@pytest.mark.parametrize('seq, val, result', REMOVE_TEST)
def test_remove(seq, val, result):
    """Test remove method for removing node associated with searched value."""
    from linked_list import LinkedList
    instance = LinkedList(seq)
    test_node = instance.search(val)
    instance.remove(test_node)
    assert instance.display() == result
