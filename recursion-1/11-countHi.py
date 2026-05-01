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
    """
    compute recursively the number of lowercase 'hi' chars in the `string`.

    Input: xxhixx  => xx xh hi ix xx    => Output: 1
                      0  0  1  0  0
    Input: xhixhix => xh hi ix xh hi ix => Output: 2
                      0  1  0  0  1  0
    Input: hi      => hi                => Output: 1
                      1
    """
    if string == "":
        return 0

    substring = string[:2]
    if substring == "hi":
        return 1 + countHi(string[1:])
    else:
        return 0 + countHi(string[1:])


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
