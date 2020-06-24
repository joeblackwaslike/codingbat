"""
allStar

Given a string, compute recursively a new string where all the adjacent chars
are now separated by a "*".


allStar("hello") → "h*e*l*l*o"
allStar("abc") → "a*b*c"
allStar("ab") → "a*b"
"""
from typing import List


def allStar(string: str) -> str:
    def recurse(s, index):
        if index > len(s) - 1:
            return ""
        if index == len(s) - 1:
            return s[index]

        return "*".join([s[index], recurse(s, index + 1)])

    return recurse(string, 0)


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ("hello", "h*e*l*l*o"),
        ("abc", "a*b*c"),
        ("ab", "a*b"),
        ("a", "a"),
        ("", ""),
        ("3.14", "3*.*1*4"),
        ("Chocolate", "C*h*o*c*o*l*a*t*e"),
        ("1234", "1*2*3*4"),
    ],
)
def test(given, expected):
    result = allStar(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
