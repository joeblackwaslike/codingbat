"""
groupSum5

https://codingbat.com/prob/p138907

Given an array of ints, is it possible to choose a group of some of the ints,
such that the group sums to the given target with these additional
constraints:

  * All multiples of 5 in the array must be included in the group.
  * If the value immediately following a multiple of 5 is 1, it must not be
    chosen. (No loops needed.)


groupSum5(0, [2, 5, 10, 4], 19) → true
groupSum5(0, [2, 5, 10, 4], 17) → true
groupSum5(0, [2, 5, 10, 4], 12) → false
"""


def groupSum5(start: int, nums: list[int], target: int) -> bool:
    pass


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ((0, [2, 5, 10, 4], 19), True),
        ((0, [2, 5, 10, 4], 17), True),
        ((0, [2, 5, 10, 4], 12), False),
        ((0, [2, 5, 4, 10], 12), False),
        ((0, [3, 5, 1], 4), False),
        ((0, [3, 5, 1], 5), True),
        ((0, [1, 3, 5], 5), True),
        ((0, [3, 5, 1], 9), False),
        ((0, [2, 5, 10, 4], 7), False),
        ((0, [2, 5, 10, 4], 15), True),
        ((0, [2, 5, 10, 4], 11), False),
        ((0, [1], 1), True),
        ((0, [9], 1), False),
        ((0, [9], 0), True),
        ((0, [], 0), True),
    ],
)
def test(given, expected):
    result = groupSum5(*given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
