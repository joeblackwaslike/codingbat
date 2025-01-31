"""
noX

https://codingbat.com/prob/p118230

Given a string, compute recursively a new string where all the 'x' chars
have been removed.


noX("xaxb") → "ab"
noX("abc") → "abc"
noX("xx") → ""
"""


def noX(string: str) -> str:
    pass


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
