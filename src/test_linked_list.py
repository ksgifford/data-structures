# # -*- coding: utf-8 -*-
import pytest


TEST_LST = [
    ([1, 2, 3], (1, 2, 3)),
    ('python', ('p', 'y', 't', 'h', 'o', 'n')),
    ([7, 8, 9], (7, 8, 9)),
    (range(100), tuple(range(100))),
]

SIZE_TEST = [
    ([0, 1, 2], 3),
    ([], 0),
    ('abcdefg', 7),
    ((0, 0, 'astring', 8, []), 5),
    (range(100), 100),
]


@pytest.mark.parametrize('seq, result', TEST_LST)
def test_init(seq, result):
    from linked_list import Linked_List
    instance = Linked_List(seq)
    assert instance.head[0] == seq[-1]


@pytest.mark.parametrize('seq, result', TEST_LST)
def test_display(seq, result):
    from linked_list import Linked_List
    instance = Linked_List(seq)
    assert instance.display() == result


@pytest.mark.parametrize('seq, result', SIZE_TEST)
def test_size(seq, result):
    from linked_list import Linked_List
    instance = Linked_List(seq)
    assert instance.size() == result
