"""
changePi

https://codingbat.com/prob/p170924

Given a string, compute recursively (no loops) a new string
where all appearances of "pi" have been replaced by "3.14".


changePi("xpix") → "x3.14x"
changePi("pipi") → "3.143.14"
changePi("pip") → "3.14p"
"""


def changePi(string: str) -> str:
    """
    compute recursively a new string where all appearances of "pi" have been replaced by "3.14".

    Input: xpix  Work: xp   pi   ix    => Output x3.14x
                       xp   3.14 ix

    Level 1:
        string: xpix
        substring: xp
        return: x + rec(pix)
    Level 2:
        string: pix
        substring: pi
        return: 3.14 + rec(x)
    Level 3:
        string: x
        substring: x
        return: x
    """
    if string == "":
        return ""
    if len(string) < 2:
        return string

    substring = string[:2]

    if substring == "pi":
        return "3.14" + changePi(string[2:])
    else:
        return string[:1] + changePi(string[1:])


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ("xpix", "x3.14x"),
        ("pipi", "3.143.14"),
        ("pip", "3.14p"),
        ("pi", "3.14"),
        ("hip", "hip"),
        ("p", "p"),
        ("x", "x"),
        ("", ""),
        ("pixx", "3.14xx"),
    ],
)
def test(given, expected):
    result = changePi(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
