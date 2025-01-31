"""
bunnyEars2

https://codingbat.com/prob/p107330

We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
(1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say have
3 ears, because they each have a raised foot. Recursively return the number
of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).


bunnyEars2(0) → 0
bunnyEars2(1) → 2
bunnyEars2(2) → 5
"""


def bunnyEars2(bunnies: int) -> int:
    pass


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        (0, 0),
        (1, 2),
        (2, 5),
    ],
)
def test(given, expected):
    result = bunnyEars2(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
