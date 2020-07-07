"""
parenBit

Given a string that contains a single pair of parenthesis, compute recursively
a new string made of only the parenthesis and their contents, so
"xyz(abc)123" yields "(abc)".


parenBit("xyz(abc)123") → "(abc)"
parenBit("x(hello)") → "(hello)"
parenBit("(xy)1") → "(xy)"
"""
from typing import List


def parenBit(string: str) -> str:
    openParen = "("
    closeParen = ")"

    def recurse(s, idx, left):
        if idx > len(s) - 1:
            return

        char = s[idx]
        if char == openParen:
            left = idx
        elif char == closeParen:
            return s[left : idx + 1]

        return recurse(s, idx + 1, left)

    return recurse(string, 0, None)


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
