"""
countAbc

https://codingbat.com/prob/p161124

Count recursively the total number of "abc" and "aba" substrings that appear
in the given string.


countAbc("abc") → 1
countAbc("abcxxabc") → 2
countAbc("abaxxaba") → 2
"""


def countAbc(string: str) -> int:
    pass


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ("abc", 1),
        ("abcxxabc", 2),
        ("abaxxaba", 2),
        ("ababc", 2),
        ("abxbc", 0),
        ("aaabc", 1),
        ("hello", 0),
        ("", 0),
        ("ab", 0),
        ("aba", 1),
        ("aca", 0),
        ("aaa", 0),
    ],
)
def test(given, expected):
    result = countAbc(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
