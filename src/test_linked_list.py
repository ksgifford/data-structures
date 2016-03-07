# # -*- coding: utf-8 -*-
import pytest


TEST_LST = [([1, 2, 3], (1, 2, 3)),
            ('python', ('p', 'y', 't', 'h', 'o', 'n')),
            ([7, 8, 9], (7, 8, 9))]


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
