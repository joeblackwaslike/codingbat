"""
count8

https://codingbat.com/prob/p192383

Given a non-negative int n, compute recursively (no loops) the count of the
occurrences of 8 as a digit, except that an 8 with another 8 immediately to
its left counts double, so 8818 yields 4. Note that mod (%) by 10 yields the
rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost
digit (126 / 10 is 12).


count8(8) → 1
count8(818) → 2
count8(8818) → 4
"""


def count8(n: int) -> int:
    if n == 0:
        return 0

    digit = n % 10
    next_n = n // 10

    is_eight = digit == 8
    next_is_eight = next_n == 8

    if is_eight and next_is_eight:
        return 2 + count8(next_n)
    elif is_eight and not next_is_eight:
        return 1 + count8(next_n)
    else:
        return 0 + count8(next_n)


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        (8, 1),
        (818, 2),
        (8818, 4),
    ],
)
def test(given, expected):
    result = count8(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
