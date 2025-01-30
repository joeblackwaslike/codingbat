"""
changeXY

https://codingbat.com/prob/p101372

Given a string, compute recursively (no loops) a new string where all the
lowercase 'x' chars have been changed to 'y' chars.


changeXY("codex") → "codey"
changeXY("xxhixx") → "yyhiyy"
changeXY("xhixhix") → "yhiyhiy"
"""


def changeXY(string: str) -> str:
    pass


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ("codex", "codey"),
        ("xxhixx", "yyhiyy"),
        ("xhixhix", "yhiyhiy"),
        ("hiy", "hiy"),
        ("h", "h"),
        ("x", "y"),
        ("", ""),
        ("xxx", "yyy"),
        ("yyhxyi", "yyhyyi"),
    ],
)
def test(given, expected):
    result = changeXY(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
