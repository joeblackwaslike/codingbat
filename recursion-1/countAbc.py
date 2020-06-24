"""
countAbc

Count recursively the total number of "abc" and "aba" substrings that appear
in the given string.


countAbc("abc") → 1
countAbc("abcxxabc") → 2
countAbc("abaxxaba") → 2
"""
from typing import List


def countAbc(string: str) -> int:
    searchStrings = dict(abc=3, aba=2)

    def recurse(s, index):
        if index > len(s) - 3:
            return 0
        subString = s[index : index + 3]

        found = subString in searchStrings
        offset = searchStrings[subString] if found else 1
        return int(found) + recurse(s, index + offset)

    return recurse(string, 0)


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
