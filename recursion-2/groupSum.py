"""
groupSum

Given an array of ints, is it possible to choose a group of some of the ints,
such that the group sums to the given target? This is a classic backtracking
recursion problem. Once you understand the recursive backtracking strategy in
this problem, you can use the same pattern for many problems to search a space
of choices. Rather than looking at the whole array, our convention is to
consider the part of the array starting at index start and continuing to the
end of the array. The caller can specify the whole array simply by passing
start as 0. No loops are needed -- the recursive calls progress down the array.


groupSum(0, [2, 4, 8], 10) → true
groupSum(0, [2, 4, 8], 14) → true
groupSum(0, [2, 4, 8], 9) → false
"""
from typing import List


def groupSum(start: int, nums: List[int], target: int) -> bool:
    if start >= len(nums):
        return target == 0

    curNum = nums[start]
    start += 1
    return groupSum(start, nums, target - curNum) or groupSum(start, nums, target)


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ((0, [2, 4, 8], 10), True),
        ((0, [2, 4, 8], 14), True),
        ((0, [2, 4, 8], 9), False),
        ((0, [2, 4, 8], 8), True),
        ((1, [2, 4, 8], 8), True),
        ((1, [2, 4, 8], 2), False),
        ((0, [1], 1), True),
        ((0, [9], 1), False),
        ((1, [9], 0), True),
        ((0, [], 0), True),
        ((0, [10, 2, 2, 5], 17), True),
        ((0, [10, 2, 2, 5], 15), True),
        ((0, [10, 2, 2, 5], 9), True),
    ],
)
def test(given, expected):
    result = groupSum(*given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
