"""
endX

Given a string, compute recursively a new string where all the lowercase 'x'
chars have been moved to the end of the string.


endX("xxre") → "rexx"
endX("xxhixx") → "hixxxx"
endX("xhixhix") → "hihixxx"
"""
from typing import List


def endX(string: str) -> str:
    def recurse(s, index, xCount):
        if index > len(s) - 1:
            if xCount:
                return "x" * xCount
            return ""

        if s[index] == "x":
            xCount += 1
            curString = ""
        else:
            curString = s[index]

        return curString + recurse(s, index + 1, xCount)

    return recurse(string, 0, 0)


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
