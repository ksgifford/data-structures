"""A quick function to determine if a string has proper parenthetics."""


def paren_test(string):
    """Iterate through a provided string and evaluate parenthetics."""
    open_count = 0
    close_count = 0

    for char in string:
        if char == '(':
            open_count += 1
        if char == ')':
            close_count += 1
            if close_count > open_count:
                return -1
    if open_count > close_count:
        return 1
    elif open_count == close_count:
        return 0
    else:
        return "ERROR"
