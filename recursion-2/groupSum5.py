"""
groupSum5

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
from typing import List


def groupSum5(start: int, nums: List[int], target: int) -> bool:
    if start >= len(nums):
        return target == 0

    curNum = nums[start]
    skip = 1

    # Must proceed with
    if curNum % 5 == 0:
        # If there is a next number, that number is 1, and not the last number
        if start + 1 < len(nums) and nums[start + 1] == 1 and start + 2 <= len(nums):
            skip += 1
        return groupSum5(start + skip, nums, target - curNum)
    else:
        # Can proceed either way
        return groupSum5(start + skip, nums, target - curNum) or groupSum5(
            start + skip, nums, target
        )


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
