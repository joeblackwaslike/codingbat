"""
bunnyEars

https://codingbat.com/prob/p183649

We have a number of bunnies and each bunny has two big floppy ears. We want to
compute the total number of ears across all the bunnies recursively (without
loops or multiplication).


bunnyEars(0) → 0
bunnyEars(1) → 2
bunnyEars(2) → 4
"""


def bunnyEars(bunnies: int) -> int:
    pass


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        (0, 0),
        (1, 2),
        (2, 4),
    ],
)
def test(given, expected):
    result = bunnyEars(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
