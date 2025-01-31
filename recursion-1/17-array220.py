"""
array220

https://codingbat.com/prob/p173469

Given an array of ints, compute recursively if the array contains somewhere a
value followed in the array by that value times 10. We'll use the convention
of considering only the part of the array that begins at the given index. In
this way, a recursive call can pass index+1 to move down the array. The
initial call will pass in index as 0.


array220([1, 2, 20], 0) → true
array220([3, 30], 0) → true
array220([3], 0) → false
"""


def array220(nums: list[int], index: int) -> bool:
    pass


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        (([1, 2, 20], 0), True),
        (([3, 30], 0), True),
        (([3], 0), False),
        (([], 0), False),
        (([3, 3, 30, 4], 0), True),
        (([2, 19, 4], 0), False),
        (([20, 2, 21], 0), False),
        (([20, 2, 21, 210], 0), True),
        (([2, 200, 2000], 0), True),
        (([0, 0], 0), True),
        (([1, 2, 3, 4, 5, 6], 0), False),
        (([1, 2, 3, 4, 5, 50, 6], 0), True),
        (([1, 2, 3, 4, 5, 51, 6], 0), False),
        (([1, 2, 3, 4, 4, 50, 500, 6], 0), True),
    ],
)
def test(given, expected):
    result = array220(*given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
