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
    pass


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
