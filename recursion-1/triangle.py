"""
triangle

https://codingbat.com/prob/p194781

We have triangle made of blocks. The topmost row has 1 block, the next row down
has 2 blocks, the next row has 3 blocks, and so on. Compute recursively (no
loops or multiplication) the total number of blocks in such a triangle with the
given number of rows.


triangle(0) → 0
triangle(1) → 1
triangle(2) → 3
"""


def triangle(rows: int) -> int:
    pass


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        (0, 0),
        (1, 1),
        (2, 3),
    ],
)
def test(given, expected):
    result = triangle(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
