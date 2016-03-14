"""Unit tests for new_deque.py module."""
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
def append_val():
    """Randomly select a value to insert, then test."""
    return random.choice([
        random.choice(range(1000)),
        random.choice(printable),
        None,
    ])


def false_case(seq):
    """Create a dict of general parameters for any False-ish test case."""
    from new_deque import Deque
    dic = {
        'display': '()',
        'size': 0,
        'pop_error': IndexError,
        'peek_val': None,
        'peekleft_val': None,
    }
    if seq is None:
        dic['instance'] = Deque()
    else:
        dic['instance'] = Deque(seq)
    return dic


def true_case(seq):
    """Create a dict of general parameters for any True-ish test case."""
    from new_deque import Deque

    return {
        'instance': Deque(seq),
        'size': len(seq),
        'size_after_pop': len(seq) - 1,
        'peek_val': seq[-1],
        'peekleft_val': seq[0],
    }


@pytest.fixture(scope='function', params=TEST_SEQUENCES)
def case_vals(request, append_val):
    """Create a dictionary of various expected values found in tests."""
    seq = request.param
    dic = {'seq': seq}

    if not seq:
        dic.update(false_case(seq))
    else:
        dic.update(true_case(seq))

    dic['size_after_append'] = dic['size'] + 1

    return dic


def test_init(case_vals):
    """Test deque constructor."""
    from new_deque import Deque
    assert isinstance(case_vals['instance'], Deque)


def test_pop_val(case_vals):
    """Test pop method to remove from back of deque."""
    instance = case_vals['instance']
    if case_vals['seq']:
        assert instance.pop() == case_vals['peek_val']


def test_pop_size(case_vals):
    """Test size after pop method is called."""
    instance = case_vals['instance']
    if case_vals['seq']:
        instance.pop()
        assert instance.size() == case_vals['size_after_pop']


def test_pop_empty(case_vals):
    """Test pop function using an empty seq."""
    instance = case_vals['instance']
    if not case_vals['seq']:
        with pytest.raises(case_vals['pop_error']):
            instance.pop()


def test_pop_left(case_vals):
    """Test popleft method to remove from front of deque."""
    instance = case_vals['instance']
    if case_vals['seq']:
        assert instance.popleft() == case_vals['peekleft_val']


def test_popleft_size(case_vals):
    """Test size after popleft method is called."""
    instance = case_vals['instance']
    if case_vals['seq']:
        instance.popleft()
        assert instance.size() == case_vals['size_after_pop']


def test_popleft_empty(case_vals):
    """Test popleft function using an empty seq."""
    instance = case_vals['instance']
    if not case_vals['seq']:
        with pytest.raises(case_vals['pop_error']):
            instance.popleft()


def test_append_size(case_vals, append_val):
    """Test append method."""
    instance = case_vals['instance']
    instance.append(append_val)
    assert instance.size() == case_vals['size_after_append']


def test_appendleft_size(case_vals, append_val):
    """Test appendleft method."""
    instance = case_vals['instance']
    instance.appendleft(append_val)
    assert instance.size() == case_vals['size_after_append']


def test_peek(case_vals):
    """Test the peek method."""
    instance = case_vals['instance']
    assert instance.peek() == case_vals['peek_val']


def test_peekleft(case_vals):
    """Test the peekleft method."""
    instance = case_vals['instance']
    assert instance.peekleft() == case_vals['peekleft_val']


def test_size(case_vals):
    """Test the size method."""
    instance = case_vals['instance']
    assert instance.size() == case_vals['size']


def test_peek_after_append(case_vals, append_val):
    """Test that peek returns the proper value after appending."""
    instance = case_vals['instance']
    instance.append(append_val)
    assert instance.pop() == append_val


def test_peekleft_after_appendleft(case_vals, append_val):
    """Test that peekleft returns the proper value after appending left."""
    instance = case_vals['instance']
    instance.appendleft(append_val)
    assert instance.popleft() == append_val
