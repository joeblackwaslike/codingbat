"""
pairStar

Given a string, compute recursively a new string where identical chars that are
adjacent in the original string are separated from each other by a "*".


pairStar("hello") → "hel*lo"
pairStar("xxyy") → "x*xy*y"
pairStar("aaaa") → "a*a*a*a"
"""
from typing import List


def pairStar(string: str) -> str:
    def recurse(s, index):
        if index > len(s) - 1:
            return ""
        if index == len(s) - 1:
            return s[index]

        if s[index] == s[index + 1]:
            return "*".join([s[index], recurse(s, index + 1)])
        else:
            return s[index] + recurse(s, index + 1)

    return recurse(string, 0)


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ("hello", "hel*lo"),
        ("xxyy", "x*xy*y"),
        ("aaaa", "a*a*a*a"),
        ("aaab", "a*a*ab"),
        ("aa", "a*a"),
        ("a", "a"),
        ("", ""),
        ("noadjacent", "noadjacent"),
        ("abba", "ab*ba"),
        ("abbba", "ab*b*ba"),
    ],
)
def test(given, expected):
    result = pairStar(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
