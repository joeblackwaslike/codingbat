"""
sumDigits

https://codingbat.com/prob/p163932

Given a non-negative int n, return the sum of its digits recursively
(no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).


sumDigits(126) → 9
sumDigits(49) → 13
sumDigits(12) → 3
"""


def sumDigits(n: int) -> int:
    pass


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        (126, 9),
        (49, 13),
        (12, 3),
    ],
)
def test(given, expected):
    result = sumDigits(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
