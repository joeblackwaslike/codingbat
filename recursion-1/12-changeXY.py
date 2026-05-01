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
    """
    compute recursively a new string where all the lowercase 'x' chars have been changed to 'y' chars.

    Input: codex  c o d e x
                  c o d e y

    Level 1:
        string: codex
        char: c
        return c + rec(odex)
    Level 2:
        string: odex
        char: o
        return: o + rec(dex)
    Level 3:
        string: dex
        char: d
        return: d + rec(ex)
    Level 4:
        string: ex
        char: e
        return: e + rec(x)
    Level 5:
        string: x
        char: x
        return: y + rec()
    Level 6:
        string: ""
        return: ""  <-- Base Case

    """
    if string == "":
        return ""

    char = string[0]

    if char == "x":
        char = "y"

    return char + changeXY(string[1:])


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
