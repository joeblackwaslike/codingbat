"""
groupSumClump

Given an array of ints, is it possible to choose a group of some of the ints,
such that the group sums to the given target, with this additional
constraint: if there are numbers in the array that are adjacent and the
identical value, they must either all be chosen, or none of them chosen.

For example, with the array {1, 2, 2, 2, 5, 2}, either all three 2's in the
middle must be chosen or not, all as a group. (one loop can be used to find
the extent of the identical values).


groupSumClump(0, [2, 4, 8], 10) → true
groupSumClump(0, [1, 2, 4, 8, 1], 14) → true
groupSumClump(0, [2, 4, 4, 8], 14) → false
"""
from typing import List


def groupSumClump(start: int, nums: List[int], target: int) -> bool:
    if start >= len(nums):
        return target == 0

    groupIdx = start
    groupSum = 0

    # Sum adjacent like numbers
    while groupIdx < len(nums) and nums[start] == nums[groupIdx]:
        groupSum += nums[groupIdx]
        groupIdx += 1

    # Proceed with or without
    return groupSumClump(groupIdx, nums, target - groupSum) or groupSumClump(
        groupIdx, nums, target
    )


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ((0, [2, 4, 8], 10), True),
        ((0, [1, 2, 4, 8, 1], 14), True),
        ((0, [2, 4, 4, 8], 14), False),
        ((0, [8, 2, 2, 1], 9), True),
        ((0, [8, 2, 2, 1], 11), False),
        ((0, [1], 1), True),
        ((0, [9], 1), False),
    ],
)
def test(given, expected):
    result = groupSumClump(*given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
