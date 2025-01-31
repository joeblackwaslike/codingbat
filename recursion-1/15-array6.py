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


def array6(nums: list[int], index: int) -> bool:
    pass


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        (([1, 6, 4], 0), True),
        (([1, 4], 0), False),
        (([6], 0), True),
        (([], 0), False),
        (([6, 2, 2], 0), True),
        (([2, 5], 0), False),
        (([1, 9, 4, 6, 6], 0), True),
        (([2, 5, 6], 0), True),
    ],
)
def test(given, expected):
    result = array6(*given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
