"""
countPairs

https://codingbat.com/prob/p154048

We'll say that a "pair" in a string is two instances of a char separated by a
char. So "AxA" the A's make a pair. Pair's can overlap, so "AxAxA" contains 3
pairs -- 2 for A and 1 for x. Recursively compute the number of pairs in the
given string.


countPairs("axa") → 1
countPairs("axax") → 2
countPairs("axbx") → 1
"""


def countPairs(string: str) -> int:
    """
    Recursively compute the number of pairs in the given string.

    A "pair" is two instances of a char separated by a char.

    Input: axa          Output: 1
    """
    if len(string) < 3:
        return 0

    if string[0] == string[2]:
        return 1 + countPairs(string[1:])
    else:
        return 0 + countPairs(string[1:])


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
