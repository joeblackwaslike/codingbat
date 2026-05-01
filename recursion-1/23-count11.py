"""
count11

https://codingbat.com/prob/p167015

Given a string, compute recursively (no loops) the number of "11" substrings
in the string. The "11" substrings should not overlap.


count11("11abc11") → 2
count11("abc11x11x11") → 3
count11("111") → 1
"""


def count11(string: str) -> int:
    if len(string) < 2:
        return 0

    if string[:2] == "11":
        return 1 + count11(string[2:])
    else:
        return 0 + count11(string[1:])


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
