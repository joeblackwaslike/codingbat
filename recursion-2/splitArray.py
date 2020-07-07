"""
splitArray

Given an array of ints, is it possible to divide the ints into two groups, so
that the sums of the two groups are the same. Every int must be in one group
or the other. Write a recursive helper method that takes whatever arguments
you like, and make the initial call to your recursive helper from
splitArray(). (No loops needed.)


splitArray([2, 2]) → true
splitArray([2, 3]) → false
splitArray([5, 2, 3]) → true
"""
from typing import List


def splitArray(nums: List[int]) -> bool:
    def recurse(idx, groupOne, groupTwo):
        if idx >= len(nums):
            return sum(groupOne) == sum(groupTwo)

        curNum = nums[idx]

        groupOne.append(curNum)
        resultOne = recurse(idx + 1, groupOne[:], groupTwo[:])
        groupOne.pop()

        groupTwo.append(curNum)
        resultTwo = recurse(idx + 1, groupOne[:], groupTwo[:])
        groupTwo.pop()

        return resultOne or resultTwo

    return recurse(0, [], [])


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ([2, 2], True),
        ([2, 3], False),
        ([5, 2, 3], True),
        ([5, 2, 2], False),
        ([1, 1, 1, 1, 1, 1], True),
        ([1, 1, 1, 1, 1], False),
        ([], True),
        ([1], False),
        ([3, 5], False),
        ([5, 3, 2], True),
        ([2, 2, 10, 10, 1, 1], True),
        ([1, 2, 2, 10, 10, 1, 1], False),
        ([1, 2, 3, 10, 10, 1, 1], True),
    ],
)
def test(given, expected):
    result = splitArray(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
