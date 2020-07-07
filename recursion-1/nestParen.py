"""
nestParen

Given a string, return true if it is a nesting of zero or more pairs of parenthesis, like "(())" or "((()))". Suggestion: check the first and last chars, and then recur on what's inside them.


nestParen("(())") → true
nestParen("((()))") → true
nestParen("(((x))") → false
"""
from typing import List


def nestParen(string: str) -> bool:
    # Edge case ""
    if not string:
        return True
    elif len(string) % 2 != 0:
        # A string with uneven length cannot be balanced
        return False

    openParen = "("
    closeParen = ")"

    def recurse(s, offset):
        left = offset
        right = len(s) - (offset + 1)

        if left > right:
            # We're done
            return True
        elif s[left] == openParen and s[right] == closeParen:
            return recurse(s, offset + 1)
        else:
            return False

    return recurse(string, 0)


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ("(())", True),
        ("((()))", True),
        ("(((x))", False),
        ("((())", False),
        ("((()()", False),
        ("()", True),
        ("", True),
        ("(yy)", False),
        ("(())", True),
        ("(((y))", False),
        ("((y)))", False),
        ("((()))", True),
        ("(())))", False),
        ("((yy())))", False),
        ("(((())))", True),
    ],
)
def test(given, expected):
    result = nestParen(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
