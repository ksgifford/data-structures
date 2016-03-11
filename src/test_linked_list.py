"""Unit tests for linked_list.py module."""
# -*- coding: utf-8 -*-
import pytest
import random
from string import printable
# from collections import defaultdict, ordereddict
# from linked_list import Node, LinkedList

TEST_NULL = 'TEST_NULL'

TEST_PARAMS = (
    'type',
    'instance',
    'popped_val',
    'pop_error',
    'display',
    'search_val',
    # 'search_result',
    'size',
)


TEST_SEQUENCES = [
    None,  # case where we construct LinkedList without passing a sequence
    'this is a much longer string sequence of characters',
    list(range(100, 1000)),
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


@pytest.fixture(scope='function')
def insert_val():
    """Randomly select a value to insert, then test."""
    return random.choice([
        random.choice(range(1000)),
        random.choice(printable),
        None,
    ])


@pytest.fixture(scope='function', params=TEST_SEQUENCES)
def assemble_dict(request, insert_val):
    """Create a dictionary of various expected values found in tests."""
    from linked_list import LinkedList
    seq = request.param
    dic = {param: TEST_NULL for param in TEST_PARAMS}

    dic['seq'] = seq

    if seq is None:
        dic['instance'] = LinkedList()
        dic['pop_error'] = IndexError
        dic['display'] = '()'
        dic['size'] = 0
    else:
        dic['search_val'] = random.choice(seq)
        dic['instance'] = LinkedList(seq)

        dic['display'] = str(tuple(reversed(seq)))

        try:
            dic['popped_val'] = seq[-1]
        except IndexError:
            dic['pop_error'] = IndexError

        dic['size'] = len(seq)

    return dic


def test_init(assemble_dict):
    """Test list constructor function with optional iterable."""
    from linked_list import LinkedList
    assert isinstance(assemble_dict['instance'], LinkedList)


def test_display(assemble_dict):
    """Test display function against sample outputs."""
    instance = assemble_dict['instance']
    assert instance.display() == assemble_dict['display']


def test_pop(assemble_dict):
    """Test pop method to remove value from head of list."""
    instance = assemble_dict['instance']
    if assemble_dict['seq']:
        assert instance.pop() == assemble_dict['popped_val']
        assert instance.size() == assemble_dict['size'] - 1
    else:
        with pytest.raises(assemble_dict['pop_error']):
            instance.pop()


def test_insert(insert_val, assemble_dict):
    """Test insert method to add value to list."""
    instance = assemble_dict['instance']
    instance.insert(insert_val)
    assert instance.head.val == insert_val


def test_search(assemble_dict):
    """Test search method for finding a given value in the list."""
    from linked_list import Node
    instance = assemble_dict['instance']
    search_val = assemble_dict['search_val']
    result = instance.search(search_val)
    assert isinstance(result, Node)
    assert result.val == search_val
    assert instance.search(TEST_NULL) == None


# @pytest.mark.parametrize('seq, val, result', REMOVE_TEST)
# def test_remove(seq, val, result):
#     """Test remove method for removing node associated with searched value."""
#     from linked_list import LinkedList
#     instance = LinkedList(seq)
#     test_node = instance.search(val)
#     instance.remove(test_node)
#     assert instance.display() == result
