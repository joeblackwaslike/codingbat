"""
stringClean

Given a string, return recursively a "cleaned" string where adjacent chars
that are the same have been reduced to a single char. So "yyzzza" yields
"yza".


stringClean("yyzzza") → "yza"
stringClean("abbbcdd") → "abcd"
stringClean("Hello") → "Helo"
"""
from typing import List


def stringClean(string: str) -> int:
    windowSize = 1

    def recurse(s, idx):
        if idx > len(s) - windowSize:
            return ""

        char = s[idx]
        if idx > 0 and char == s[idx - 1]:
            char = ""

        return char + recurse(s, idx + 1)

    return recurse(string, 0)


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
