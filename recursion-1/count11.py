"""
count11

Given a string, compute recursively (no loops) the number of "11" substrings
in the string. The "11" substrings should not overlap.


count11("11abc11") → 2
count11("abc11x11x11") → 3
count11("111") → 1
"""
from typing import List


def count11(string: str) -> int:
    searchString = "11"
    windowSize = len(searchString)

    def recurse(s, idx):
        if idx > len(s) - windowSize:
            return 0
        subString = s[idx : idx + windowSize]

        found = subString == searchString
        offset = 2 if found else 1
        return int(found) + recurse(s, idx + offset)

    return recurse(string, 0)


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ("11abc11", 2),
        ("abc11x11x11", 3),
        ("111", 1),
        ("1111", 2),
        ("1", 0),
        ("", 0),
        ("hi", 0),
        ("11x111x1111", 4),
        ("1x111", 1),
        ("1Hello1", 0),
        ("Hello", 0),
    ],
)
def test(given, expected):
    result = count11(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
