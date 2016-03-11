"""Test suite for the Stack data type."""
import pytest
import random
from string import printable

TEST_NULL = 'TEST_NULL'

TEST_SEQUENCES = [
    None,  # case where we construct Stack without passing a sequence
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
def push_val():
    """Randomly select a value to , then test."""
    return random.choice([
        random.choice(range(1000)),
        random.choice(printable),
        None,
    ])


def false_case(seq, push_val):
    """Create a dict of general parameters for any False-ish test case."""
    from stack import Stack
    dic = {
        'pop_error': IndexError,
    }
    if seq is None:
        dic['instance'] = Stack()
    else:
        dic['instance'] = Stack(seq),
        dic['display_after_push'] = str(tuple(reversed(seq)) + (push_val,))
    return dic


def true_case(seq, push_val):
    """Create a dict of general parameters for any True-ish test case."""
    from stack import Stack
    rev_seq = seq[::-1]

    return {
        'instance': Stack(seq),
        'popped_val': seq[-1],
        'display': str(tuple(rev_seq)),
        'display_after_pop': str(tuple(rev_seq[1:])),
        'display_after_push': str(tuple(rev_seq) + (push_val,))
    }


@pytest.fixture(scope='function', params=TEST_SEQUENCES)
def case_vals(request, push_val):
    """Create a dictionary of various expected values found in tests."""
    seq = request.param
    dic = {'seq': seq}

    if not seq:
        dic.update(false_case(seq, push_val))
    else:
        dic.update(true_case(seq, push_val))
    return dic


def test_init(case_vals):
    """Test class constructor of Stack."""
    from stack import Stack
    instance = case_vals['instance']
    assert isinstance(instance, Stack)


def test_push(push_val, case_vals):
    """Test push method of Stack."""
    instance = case_vals['instance']
    instance.push(push_val)
    assert instance._stack.display() == case_vals['display_after_push']


def test_pop(case_vals):
    """Test pop method of Stack."""
    instance = case_vals['instance']
    if case_vals['seq']:
        assert instance.pop() == case_vals['popped_val']
        assert instance._stack.display() == case_vals['display_after_pop']
    else:
        with pytest.rase(case_vals['pop_error']):
            instance.pop()


def test_push_and_pop(case_vals):
    """Test that pop() returns the last value pushed to the stack."""
    instance = case_vals['instance']
    init_display = instance._stack.display()
    instance.push(push_val)
    assert instance._stack.display() == case_vals['display_after_push']
    assert instance.pop() == push_val
    assert instance._stack.display() == init_display
