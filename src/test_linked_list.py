"""Unit tests for linked_list.py module."""
# -*- coding: utf-8 -*-
import pytest
import random
from string import printable

TEST_NULL = 'TEST_NULL'

TEST_SEQUENCES = [
    None,  # case where we construct LinkedList without passing a sequence
    'this is a much longer string sequence of characters',
    'smaller str',
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


def false_case(seq):
    """Create a dict of general parameters for any False-ish test case."""
    from linked_list import LinkedList
    dic = {
        'display': '()',
        'size': 0,
        'pop_error': IndexError,
        'remove_error': ValueError,
        'search_val': TEST_NULL,
    }
    if seq is None:
        dic['instance'] = LinkedList()
    else:
        dic['instance'] = LinkedList(seq)
    return dic


def true_case(seq):
    """Create a dict of general parameters for any True-ish test case."""
    from linked_list import LinkedList
    search_val = random.choice(seq)
    rev_seq = seq[::-1]
    last_idx = rev_seq.index(search_val)

    return {
        'instance': LinkedList(seq),
        'size': len(seq),
        'search_val': search_val,
        'popped_val': seq[-1],
        'display': str(tuple(rev_seq)),
        'display_after_pop': str(tuple(rev_seq[1:])),
        'display_after_remove': str(tuple(
            rev_seq[:last_idx] + rev_seq[last_idx + 1:])),
    }


@pytest.fixture(scope='function', params=TEST_SEQUENCES)
def case_vals(request, insert_val):
    """Create a dictionary of various expected values found in tests."""
    seq = request.param
    dic = {'seq': seq}

    if not seq:
        dic.update(false_case(seq))
    else:
        dic.update(true_case(seq))
    return dic


def test_init(case_vals):
    """Test list constructor function with optional iterable."""
    from linked_list import LinkedList
    assert isinstance(case_vals['instance'], LinkedList)


def test_display(case_vals):
    """Test display function against sample outputs."""
    instance = case_vals['instance']
    assert instance.display() == case_vals['display']


def test_pop(case_vals):
    """Test pop method to remove value from head of list."""
    instance = case_vals['instance']
    if case_vals['seq']:
        assert instance.pop() == case_vals['popped_val']
        assert instance.size() == case_vals['size'] - 1
        assert instance.display() == case_vals['display_after_pop']
    else:
        with pytest.raises(case_vals['pop_error']):
            instance.pop()


def test_insert(insert_val, case_vals):
    """Test insert method to add value to list."""
    instance = case_vals['instance']
    instance.insert(insert_val)
    assert instance.head.val == insert_val


def test_search(case_vals):
    """Test search method for finding a given value in the list."""
    from linked_list import Node
    instance = case_vals['instance']
    search_val = case_vals['search_val']
    result = instance.search(search_val)
    if case_vals['seq']:
        assert isinstance(result, Node)
        assert result.val == search_val
    else:
        assert result is None
    assert instance.search(TEST_NULL) is None


def test_remove(case_vals):
    """Test remove method for removing node associated with searched value."""
    from linked_list import Node
    instance = case_vals['instance']
    search_val = case_vals['search_val']
    seq = case_vals['seq']
    remove_node = instance.search(search_val)
    if not seq or search_val not in seq:
        with pytest.raises(case_vals['remove_error']):
            instance.remove(Node(TEST_NULL))
    else:
        instance.remove(remove_node)
        assert instance.size() == len(seq) - 1
        assert instance.display() == case_vals['display_after_remove']
