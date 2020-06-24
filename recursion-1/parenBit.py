"""
parenBit

Given a string that contains a single pair of parenthesis, compute recursively
a new string made of only of the parenthesis and their contents, so
"xyz(abc)123" yields "(abc)".


parenBit("xyz(abc)123") → "(abc)"
parenBit("x(hello)") → "(hello)"
parenBit("(xy)1") → "(xy)"
"""
from typing import List


def parenBit(string: str) -> str:
    openParen = "("
    closeParen = ")"

    def recurse(s, idx, newStr, opened, closed):
        char = s[idx]
        opening = not opened and char == openParen
        closing = not closed and char == closeParen

        if opened and closed:
            return newStr
        elif any([opening, closing, opened]):
            newStr += char

        recurse(s, idx + 1, newStr, opened or opening, closed or closing)

    return recurse(string, 0, "", False, False)


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ("xyz(abc)123", "(abc)"),
        ("x(hello)", "(hello)"),
        ("(xy)1", "(xy)"),
        ("not really (possible)", "(possible)"),
        ("(abc)", "(abc)"),
        ("(abc)xyz", "(abc)"),
        ("(abc)x", "(abc)"),
        ("(x)", "(x)"),
        ("()", "()"),
        ("res (ipsa) loquitor", "(ipsa)"),
        ("hello(not really)there", "(not really)"),
        ("ab(ab)ab", "(ab)"),
    ],
)
def test(given, expected):
    result = parenBit(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
