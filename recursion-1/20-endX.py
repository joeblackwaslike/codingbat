"""
endX

https://codingbat.com/prob/p105722

Given a string, compute recursively a new string where all the lowercase 'x'
chars have been moved to the end of the string.


endX("xxre") → "rexx"
endX("xxhixx") → "hixxxx"
endX("xhixhix") → "hihixxx"
"""


def endX(string: str) -> str:
    """
    compute recursively a new string where all the 'x' chars have been moved to the end of the string.

    Input: xxre    Work: 1  rec(x++) + x              Output: rexx
                         2  rec(x++) + x + x
                         3  r + rec(x++) + x + x
                         4  r + e + x + x

    Level 1:
        index: 0
        char: x
        return: rec(index + 1) + x
    Level 2:
        index: 1
        char: x
        return: rec(index + 1) + x
    Level 3:
        index: 2
        char: r
        return: r + rec(index + 1)
    Level 4:
        index: 3
        char: e
        return: e + rec(index + 1)
    """

    if len(string) == 0:
        return ""

    if string[0] == "x":
        return endX(string[1:]) + "x"
    else:
        return string[0] + endX(string[1:])


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ("xxre", "rexx"),
        ("xxhixx", "hixxxx"),
        ("xhixhix", "hihixxx"),
        ("hiy", "hiy"),
        ("h", "h"),
        ("x", "x"),
        ("xx", "xx"),
        ("", ""),
        ("bxx", "bxx"),
        ("bxax", "baxx"),
        ("axaxax", "aaaxxx"),
        ("xxhxi", "hixxx"),
    ],
)
def test(given, expected):
    result = endX(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
