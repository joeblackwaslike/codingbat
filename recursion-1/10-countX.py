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
    """
    compute recursively the number of lowercase 'x' chars in the `string`.

    Input: "xxhixx"  Output: 4
    """

    if string == "":
        return 0

    char, rest = string[0], string[1:]

    if char == "x":
        return 1 + countX(rest)
    else:
        return 0 + countX(rest)


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
