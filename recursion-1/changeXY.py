"""
changeXY

Given a string, compute recursively (no loops) a new string where all the
lowercase 'x' chars have been changed to 'y' chars.


changeXY("codex") → "codey"
changeXY("xxhixx") → "yyhiyy"
changeXY("xhixhix") → "yhiyhiy"
"""


def changeXY(string):
    if not string:
        return string
    elif len(string) == 1:
        return "y" if string == "x" else string
    else:
        return changeXY(string[0]) + changeXY(string[1:])


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
