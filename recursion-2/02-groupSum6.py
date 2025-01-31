"""
groupSum6

https://codingbat.com/prob/p199368

Given an array of ints, is it possible to choose a group of some of the ints,
beginning at the start index, such that the group sums to the given target?
However, with the additional constraint that all 6's must be chosen. (No
loops needed.)


groupSum6(0, [5, 6, 2], 8) → true
groupSum6(0, [5, 6, 2], 9) → false
groupSum6(0, [5, 6, 2], 7) → false
"""


def groupSum6(start: int, nums: list[int], target: int) -> bool:
    pass


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
