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
    pass


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
