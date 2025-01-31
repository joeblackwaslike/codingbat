"""
strCount

https://codingbat.com/prob/p186177

Given a string and a non-empty substring sub, compute recursively the number
of times that sub appears in the string, without the sub strings overlapping.


strCount("catcowcat", "cat") → 2
strCount("catcowcat", "cow") → 1
strCount("catcowcat", "dog") → 0
"""


def strCount(string: str) -> int:
    pass


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        (("catcowcat", "cat"), 2),
        (("catcowcat", "cow"), 1),
        (("catcowcat", "dog"), 0),
        (("cacatcowcat", "cat"), 2),
        (("xyx", "x"), 2),
        (("iiiijj", "i"), 4),
        (("iiiijj", "ii"), 2),
        (("iiiijj", "iii"), 1),
        (("iiiijj", "j"), 2),
        (("iiiijj", "jj"), 1),
        (("aaabababab", "ab"), 4),
        (("aaabababab", "aa"), 1),
        (("aaabababab", "a"), 6),
        (("aaabababab", "b"), 4),
    ],
)
def test(given, expected):
    result = strCount(*given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
