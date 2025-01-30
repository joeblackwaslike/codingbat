"""
count7

https://codingbat.com/prob/p101409

Given a non-negative int n, return the count of the occurrences of 7 as a
digit, so for example 717 yields 2. (no loops). Note that mod (%) by 10 yields
the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the
rightmost digit (126 / 10 is 12).


count7(717) → 2
count7(7) → 1
count7(123) → 0
"""


def count7(n: int) -> int:
    pass


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        (717, 2),
        (7, 1),
        (123, 0),
    ],
)
def test(given, expected):
    result = count7(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
