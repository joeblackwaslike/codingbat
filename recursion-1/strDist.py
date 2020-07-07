"""
strDist

Given a string and a non-empty substring sub, compute recursively the largest
substring which starts and ends with sub and return its length.


strDist("catcowcat", "cat") → 9
strDist("catcowcat", "cow") → 3
strDist("cccatcowcatxx", "cat") → 9
"""
from typing import List


def strDist(string: str, sub: str) -> int:
    """Uses start, end indexes and keeps start sticky by keeping track of count."""
    strLen = len(string)
    subLen = len(sub)

    def recurse(s, idx, start, end, count):
        left = idx
        right = idx + subLen
        if right > strLen:
            return end - start

        if s[left:right] == sub:
            if count == 0:
                start = left
            count += 1
            end = right

        return recurse(s, idx + 1, start, end, count)

    return recurse(string, 0, 0, 0, 0)


def strDistSlice(string: str, sub: str) -> int:
    """Uses python's seldom used slice object to keep track of indexes."""
    strLen = len(string)
    subLen = len(sub)

    def recurse(s, idx, subSlice):
        curSlice = slice(idx, idx + subLen)
        if curSlice.stop > strLen:
            return subSlice.stop - subSlice.start if subSlice else 0

        if s[curSlice] == sub:
            if not subSlice:
                subSlice = slice(curSlice.start, curSlice.stop)
            else:
                subSlice = slice(subSlice.start, curSlice.stop)

        return recurse(s, idx + 1, subSlice)

    return recurse(string, 0, None)


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        (("catcowcat", "cat"), 9),
        (("catcowcat", "cow"), 3),
        (("cccatcowcatxx", "cat"), 9),
        (("abccatcowcatcatxyz", "cat"), 12),
        (("xyx", "x"), 3),
        (("xyx", "y"), 1),
        (("xyx", "z"), 0),
        (("z", "z"), 1),
        (("x", "z"), 0),
        (("", "z"), 0),
        (("hiHellohihihi", "hi"), 13),
        (("hiHellohihihi", "hih"), 5),
        (("hiHellohihihi", "o"), 1),
        (("hiHellohihihi", "ll"), 2),
    ],
)
@pytest.mark.parametrize("solution", [strDist, strDistSlice])
def test(given, expected, solution):
    result = solution(*given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
