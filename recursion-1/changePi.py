"""
changePi

Given a string, compute recursively (no loops) a new string
where all appearances of "pi" have been replaced by "3.14".


changePi("xpix") → "x3.14x"
changePi("pipi") → "3.143.14"
changePi("pip") → "3.14p"
"""


def changePi(string):
    def recurse(s, output=""):
        if not s:
            return output
        elif s.startswith("pi"):
            output += "3.14"
            return recurse(s[2:], output)
        else:
            output += s[0]
            return recurse(s[1:], output)

    return recurse(string)


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
