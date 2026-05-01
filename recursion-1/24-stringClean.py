"""
stringClean

https://codingbat.com/prob/p104029

Given a string, return recursively a "cleaned" string where adjacent chars
that are the same have been reduced to a single char. So "yyzzza" yields
"yza".


stringClean("yyzzza") → "yza"
stringClean("abbbcdd") → "abcd"
stringClean("Hello") → "Helo"
"""


def stringClean(string: str) -> str:
    """
    return recursively a "cleaned" string where adjacent chars that are the same have been reduced to a single char.

    Input: yyzzza     Output: yza

    Level 1:
        index: 0
        first_char: y
        next_char: y
        return: "" + stringClean(string, index + 1)
    Level 2:
        index: 1
        first_char: y
        next_char:
        return:
    Level 3:
        index:
        first_char:
        next_char:
        return:
    Level 4:
        index:
        first_char:
        next_char:
        return:
    Level 5:
        index:
        first_char:
        next_char:
        return:
    """

    # if only one char left just return it
    if len(string) == 1:
        return string

    if string[1] == string[0]:
        return "" + stringClean(string[1:])
    else:
        return string[0] + stringClean(string[1:])


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ("yyzzza", "yza"),
        ("abbbcdd", "abcd"),
        ("Hello", "Helo"),
        ("XXabcYY", "XabcY"),
        ("112ab445", "12ab45"),
        ("Hello Bookkeeper", "Helo Bokeper"),
    ],
)
def test(given, expected):
    result = stringClean(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
