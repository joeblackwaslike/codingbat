"""
array11

Given an array of ints, compute recursively the number of times that the
value 11 appears in the array. We'll use the convention of considering only
the part of the array that begins at the given index. In this way, a recursive
call can pass index+1 to move down the array. The initial call will pass in
index as 0.


array11([1, 2, 11], 0) → 1
array11([11, 11], 0) → 2
array11([1, 2, 3, 4], 0) → 0
"""
from typing import List


def array11(nums: List[int], index: int) -> int:
    if index > len(nums) - 1:
        return 0
    return int(nums[index] == 11) + array11(nums, index + 1)


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        (([1, 2, 11], 0), 1),
        (([11, 11], 0), 2),
        (([1, 2, 3, 4], 0), 0),
        (([1, 11, 3, 11, 11], 0), 3),
        (([11], 0), 1),
        (([1], 0), 0),
        (([], 0), 0),
        (([11, 2, 3, 4, 11, 5], 0), 2),
        (([11, 5, 11], 0), 2),
    ],
)
def test(given, expected):
    result = array11(*given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
