"""Unit tests for parenthetics_kevin.py module."""
# -*- coding: utf-8 -*-


TEST_STRINGS = [
    '((Here is) a (working) string).',
    '(Here is an(open) (string).',
    'Here is) a (broken)(string.',
]


def test_working_str():
    """Test for a string with properly opening and closing parenthetics."""
    from parenthetics_kevin import paren_test
    assert paren_test(TEST_STRINGS[0]) == 0


def test_open_str():
    """Test for a string with open parenthetics."""
    from parenthetics_kevin import paren_test
    assert paren_test(TEST_STRINGS[1]) == 1


def test_broken_str():
    """Test for a string with broken parenthetics."""
    from parenthetics_kevin import paren_test
    assert paren_test(TEST_STRINGS[2]) == -1
