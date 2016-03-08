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
