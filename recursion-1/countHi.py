"""
countHi

https://codingbat.com/prob/p184029

Given a string, compute recursively (no loops) the number of lowercase 'hi' chars
in the string.


countHi("xxhixx") → 1
countHi("xhixhix") → 2
countHi("hi") → 1
"""


def countHi(string: str) -> int:
    pass


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ("xxhixx", 1),
        ("xhixhix", 2),
        ("hi", 1),
        ("hihih", 2),
        ("h", 0),
        ("ihihihihih", 4),
        ("hihihihihi", 5),
        ("hiAAhi12hi", 3),
        ("xhixhxihihhhih", 3),
    ],
)
def test(given, expected):
    result = countHi(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
