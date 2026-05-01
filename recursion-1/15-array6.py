"""
array6

https://codingbat.com/prob/p108997

Given an array of ints, compute recursively if the array contains a 6. We'll
use the convention of considering only the part of the array that begins at
the given index. In this way, a recursive call can pass index+1 to move down
the array. The initial call will pass in index as 0.


array6([1, 6, 4], 0) → true
array6([1, 4], 0) → false
array6([6], 0) → true
"""


def array6(nums: list[int]) -> bool:
    """
    compute recursively if `nums` array contains a 6

    Input:
        nums: [1, 6, 4]  Work:
                            1         6
                            False or  True ..
                            index: 0  Index: 1

    Global:
        nums: [1, 6, 4]

    Level 1:
        index: 0
        value: 1
        return: False or rec([1, 6, 4], 1)
    Level 2:
        index: 1
        value: 6
        return: True // or rec([1, 6, 4], 2)

    """

    if len(nums) == 0:
        return False

    if nums[0] == 6:
        return True or array6(nums[1:])
    else:
        return False or array6(nums[1:])


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ([1, 6, 4], True),
        ([1, 4], False),
        ([6], True),
        ([], False),
        ([6, 2, 2], True),
        ([2, 5], False),
        ([1, 9, 4, 6, 6], True),
        ([2, 5, 6], True),
    ],
)
def test(given, expected):
    result = array6(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
