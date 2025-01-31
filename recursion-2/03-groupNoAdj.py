"""
groupNoAdj

https://codingbat.com/prob/p169605

Given an array of ints, is it possible to choose a group of some of the ints,
such that the group sums to the given target with this additional constraint:

  If a value in the array is chosen to be in the group, the value immediately
  following it in the array must not be chosen. (No loops needed.)


groupNoAdj(0, [2, 5, 10, 4], 12) → true
groupNoAdj(0, [2, 5, 10, 4], 14) → false
groupNoAdj(0, [2, 5, 10, 4], 7) → false
"""


def groupNoAdj(start: int, nums: list[int], target: int) -> bool:
    pass


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ((0, [2, 5, 10, 4], 12), True),
        ((0, [2, 5, 10, 4], 14), False),
        ((0, [2, 5, 10, 4], 7), False),
        ((0, [2, 5, 10, 4, 2], 7), True),
        ((0, [2, 5, 10, 4], 9), True),
        ((0, [10, 2, 2, 3, 3], 15), True),
        ((0, [10, 2, 2, 3, 3], 7), False),
        ((0, [], 0), True),
        ((0, [1], 1), True),
        ((0, [9], 1), False),
        ((0, [9], 0), True),
        ((0, [5, 10, 4, 1], 11), True),
    ],
)
def test(given, expected):
    result = groupNoAdj(*given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
