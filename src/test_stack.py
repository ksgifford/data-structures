"""Test suite for the Stack data type."""
import pytest

TEST_INIT = [
    ([1, 2, 3, 4],),
    ('abcd',),
    ((),),
]


TEST_PUSH = [
    ([0, 1, 2], 'a', ('a', 2, 1, 0)),
    ('defg', 1, (1, 'g', 'f', 'e', 'd')),
    ((0, 0, 'astring', 8, []), 0, (0, [], 8, 'astring', 0, 0)),
    ([], [], ([],)),
]


TEST_POP = [
    ([0, 1, 2], 2, (1, 0)),
    ('defg', 'g', ('f', 'e', 'd')),
    ((0, 0, 'astring', 8, []), [], (8, 'astring', 0, 0)),
    ([], [], [])
]


TEST_PUSH_POP = [
    ([0, 1, 2], 'a', 'a'),
    ('defg', 1, 1),
    ((0, 0, 'astring', 8, []), 0, 0),
]


@pytest.mark.parametrize('seq', TEST_INIT)
def test_init(seq):
    """Test class constructor of Stack."""
    from stack import Stack
    instance = Stack(seq)
    assert isinstance(instance, Stack)


@pytest.mark.parametrize('seq, val, result', TEST_PUSH)
def test_push(seq, val, result):
    """Test push method of Stack."""
    from stack import Stack
    instance = Stack(seq)
    instance.push(val)
    assert instance._stack.display() == result


@pytest.mark.parametrize('seq, return_val, display_lst', TEST_POP)
def test_pop(seq, return_val, display_lst):
    """Test pop method of Stack."""
    from stack import Stack
    instance = Stack(seq)
    try:
        assert instance.pop() == return_val
        assert instance._stack.display() == display_lst
    except Exception as e:
        if not seq:
            assert isinstance(e, IndexError)
        else:
            raise e


@pytest.mark.parametrize('seq, push_val, pop_val', TEST_PUSH_POP)
def test_push_and_pop(seq, push_val, pop_val):
    """Test that pop() returns the last value pushed to the stack."""
    from stack import Stack
    instance = Stack(seq)
    instance.push(push_val)
    assert instance.pop() == pop_val
