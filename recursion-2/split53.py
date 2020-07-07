"""
split53

Given an array of ints, is it possible to divide the ints into two groups, so
that the sum of the two groups is the same, with these constraints: all the
values that are multiple of 5 must be in one group, and all the values that
are a multiple of 3 (and not a multiple of 5) must be in the other. (No loops
needed.)


split53([1, 1]) → true
split53([1, 1, 1]) → false
split53([2, 4, 2]) → true
"""
from typing import List


def split53(nums: List[int]) -> bool:
    def recurse(idx, groupOne, groupTwo):
        if idx >= len(nums):
            return sum(groupOne) == sum(groupTwo)

        curNum = nums[idx]

        if curNum % 5 == 0:
            groupOne.append(curNum)
            return recurse(idx + 1, groupOne[:], groupTwo[:])
        elif curNum % 3 == 0:
            groupTwo.append(curNum)
            return recurse(idx + 1, groupOne[:], groupTwo[:])
        else:
            groupOne.append(curNum)
            resultOne = recurse(idx + 1, groupOne[:], groupTwo[:])
            groupOne.pop()

            groupTwo.append(curNum)
            return resultOne or recurse(idx + 1, groupOne[:], groupTwo[:])

    return recurse(0, [], [])


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
