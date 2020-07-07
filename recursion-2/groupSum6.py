"""
groupSum6

Given an array of ints, is it possible to choose a group of some of the ints,
beginning at the start index, such that the group sums to the given target?
However, with the additional constraint that all 6's must be chosen. (No
loops needed.)


groupSum6(0, [5, 6, 2], 8) → true
groupSum6(0, [5, 6, 2], 9) → false
groupSum6(0, [5, 6, 2], 7) → false
"""
from typing import List


def groupSum6(start: int, nums: List[int], target: int) -> bool:
    if start >= len(nums):
        return target == 0

    curNum = nums[start]
    start += 1
    if curNum == 6:
        # Must proceed only with
        return groupSum6(start, nums, target - curNum)
    else:
        # Can proceed either way
        return groupSum6(start, nums, target - curNum) or groupSum6(start, nums, target)


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ((0, [5, 6, 2], 8), True),
        ((0, [5, 6, 2], 9), False),
        ((0, [5, 6, 2], 7), False),
        ((0, [1], 1), True),
        ((0, [9], 1), False),
        ((0, [], 0), True),
        ((0, [3, 2, 4, 6], 8), True),
        ((0, [6, 2, 4, 3], 8), True),
        ((0, [5, 2, 4, 6], 9), False),
        ((0, [6, 2, 4, 5], 9), False),
        ((0, [3, 2, 4, 6], 3), False),
        ((0, [1, 6, 2, 6, 4], 12), True),
        ((0, [1, 6, 2, 6, 4], 13), True),
        ((0, [1, 6, 2, 6, 4], 4), False),
        ((0, [1, 6, 2, 6, 4], 9), False),
        ((0, [1, 6, 2, 6, 5], 14), True),
        ((0, [1, 6, 2, 6, 5], 15), True),
        ((0, [1, 6, 2, 6, 5], 16), False),
    ],
)
def test(given, expected):
    result = groupSum6(*given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
