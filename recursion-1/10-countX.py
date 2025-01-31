"""
countX

https://codingbat.com/prob/p170371

Given a string, compute recursively (no loops) the number of lowercase 'x' chars
in the string.


countX("xxhixx") → 4
countX("xhixhix") → 3
countX("hi") → 0
"""


def countX(string: str) -> int:
    pass


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ("xxhixx", 4),
        ("xhixhix", 3),
        ("hi", 0),
    ],
)
def test(given, expected):
    result = countX(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
