"""
noX

Given a string, compute recursively a new string where all the 'x' chars
have been removed.


noX("xaxb") → "ab"
noX("abc") → "abc"
noX("xx") → ""
"""


def noX(string):
    if not string:
        return ""
    elif len(string) == 1:
        return string if string != "x" else ""

    return noX(string[0]) + noX(string[1:])


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ("xaxb", "ab"),
        ("abc", "abc"),
        ("xx", ""),
        ("", ""),
        ("axxbxx", "ab"),
        ("Hellox", "Hello"),
    ],
)
def test(given, expected):
    result = noX(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
