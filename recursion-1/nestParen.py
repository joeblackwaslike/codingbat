"""
nestParen

https://codingbat.com/prob/p183174

Given a string, return true if it is a nesting of zero or more pairs of parenthesis, like "(())" or "((()))". Suggestion: check the first and last chars, and then recur on what's inside them.


nestParen("(())") → true
nestParen("((()))") → true
nestParen("(((x))") → false
"""


def nestParen(string: str) -> bool:
    pass


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
