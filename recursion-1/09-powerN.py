"""
powerN

https://codingbat.com/prob/p158888

Given base and n that are both 1 or more, compute recursively (no loops) the
value of base to the n power, so powerN(3, 2) is 9 (3 squared).

powerN(3, 1) → 3
powerN(3, 2) → 9
powerN(3, 3) → 27

"""


def powerN(base: int, n: int) -> int:
    """
    Compute recursively the value of base to the nth power.

    Inputs: base=3, n=1  => Work: 3         = 3
            base=3, n=2  => Work: 3 * 3     = 9
            base=3, n=3  => Work: 3 * 3 * 3 = 27
    """
    if n == 1:
        return base

    return base * powerN(base, n - 1)


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ((3, 1), 3),
        ((3, 2), 9),
        ((3, 3), 27),
    ],
)
def test(given, expected):
    result = powerN(*given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
