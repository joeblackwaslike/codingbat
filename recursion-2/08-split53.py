"""
split53

https://codingbat.com/prob/p168295

Given an array of ints, is it possible to divide the ints into two groups, so
that the sum of the two groups is the same, with these constraints: all the
values that are multiple of 5 must be in one group, and all the values that
are a multiple of 3 (and not a multiple of 5) must be in the other. (No loops
needed.)


split53([1, 1]) → true
split53([1, 1, 1]) → false
split53([2, 4, 2]) → true
"""


def split53(nums: list[int]) -> bool:
    pass


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ([1, 1], True),
        ([1, 1, 1], False),
        ([2, 4, 2], True),
        ([2, 2, 2, 1], False),
        ([3, 3, 5, 1], True),
        ([3, 5, 8], False),
        ([2, 4, 6], True),
        ([3, 5, 6, 10, 3, 3], True),
    ],
)
def test(given, expected):
    result = split53(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
