"""
pairStar

https://codingbat.com/prob/p158175

Given a string, compute recursively a new string where identical chars that are
adjacent in the original string are separated from each other by a "*".


pairStar("hello") → "hel*lo"
pairStar("xxyy") → "x*xy*y"
pairStar("aaaa") → "a*a*a*a"
"""


def pairStar(string: str, index: int = 0) -> str:
    """
    compute recursively a new string where identical adjacent chars are separated from each other by "*".

    Input: hello        Output: hel*lo

    Level 1:
        index: 0
        char: h
        next_char: e
        return: h + rec(index + 1)
    Level 2:
        index: 1
        char: e
        next_char: l
        return: e + recurse(index + 1)
    Level 3:
        index: 2
        char: l
        next_char: l
        return: l* + recurse(index + 1)
    Level 4:
        index: 3
        char: l
        next_char: o
        return: l + recurse(index + 1)
    Level 5:
        index: 4
        return: o

    """
    if index == len(string):
        return ""
    elif index == len(string) - 1:
        return string[index]

    char = string[index]
    next_char = string[index + 1]

    if char == next_char:
        return char + "*" + pairStar(string, index + 1)
    else:
        return char + pairStar(string, index + 1)


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ("hello", "hel*lo"),
        ("xxyy", "x*xy*y"),
        ("aaaa", "a*a*a*a"),
        ("aaab", "a*a*ab"),
        ("aa", "a*a"),
        ("a", "a"),
        ("", ""),
        ("noadjacent", "noadjacent"),
        ("abba", "ab*ba"),
        ("abbba", "ab*b*ba"),
    ],
)
def test(given, expected):
    result = pairStar(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
