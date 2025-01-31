"""
splitOdd10

https://codingbat.com/prob/p171660

Given an array of ints, is it possible to divide the ints into two groups, so
that the sum of one group is a multiple of 10, and the sum of the other group
is odd. Every int must be in one group or the other. Write a recursive helper
method that takes whatever arguments you like, and make the initial call to
your recursive helper from splitOdd10(). (No loops needed.)


splitOdd10([5, 5, 5]) → true
splitOdd10([5, 5, 6]) → false
splitOdd10([5, 5, 6, 1]) → true
"""


def splitOdd10(nums: list[int]) -> bool:
    pass


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ([5, 5, 5], True),
        ([5, 5, 6], False),
        ([5, 5, 6, 1], True),
        ([6, 5, 5, 1], True),
        ([6, 5, 5, 1, 10], True),
        ([6, 5, 5, 5, 1], False),
        ([1], True),
        ([], False),
        ([10, 7, 5, 5], True),
        ([10, 0, 5, 5], False),
        ([10, 7, 5, 5, 2], True),
        ([10, 7, 5, 5, 1], False),
    ],
)
def test(given, expected):
    result = splitOdd10(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
