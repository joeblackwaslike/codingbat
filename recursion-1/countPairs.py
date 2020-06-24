"""
countPairs

We'll say that a "pair" in a string is two instances of a char separated by a
char. So "AxA" the A's make a pair. Pair's can overlap, so "AxAxA" contains 3
pairs -- 2 for A and 1 for x. Recursively compute the number of pairs in the
given string.


countPairs("axa") → 1
countPairs("axax") → 2
countPairs("axbx") → 1
"""
from typing import List


def countPairs(string: str) -> int:
    def recurse(s, index):
        if index > len(s) - 3:
            return 0
        isPair = 1 if s[index] == s[index + 2] else 0
        return isPair + recurse(s, index + 1)

    return recurse(string, 0)


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ("axa", 1),
        ("axax", 2),
        ("axbx", 1),
        ("hi", 0),
        ("hihih", 3),
        ("ihihhh", 3),
        ("ihjxhh", 0),
        ("", 0),
        ("a", 0),
        ("aa", 0),
        ("aaa", 1),
    ],
)
def test(given, expected):
    result = countPairs(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
