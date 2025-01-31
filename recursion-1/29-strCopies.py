"""
strCopies

https://codingbat.com/prob/p118182

Given a string and a non-empty substring sub, compute recursively if at least n
copies of sub appear in the string somewhere, possibly with overlapping. N will
be non-negative.


strCopies("catcowcat", "cat", 2) → true
strCopies("catcowcat", "cow", 2) → false
strCopies("catcowcat", "cow", 1) → true
"""


def strCopies(string: str, sub: str, n: int) -> bool:
    pass


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        (("catcowcat", "cat", 2), True),
        (("catcowcat", "cow", 2), False),
        (("catcowcat", "cow", 1), True),
        (("iiijjj", "i", 3), True),
        (("iiijjj", "i", 4), False),
        (("iiijjj", "ii", 2), True),
        (("iiijjj", "ii", 3), False),
        (("iiijjj", "x", 3), False),
        (("iiijjj", "x", 0), True),
        (("iiiiij", "iii", 3), True),
        (("iiiiij", "iii", 4), False),
        (("ijiiiiij", "iiii", 2), True),
        (("ijiiiiij", "iiii", 3), False),
        (("dogcatdogcat", "dog", 2), True),
    ],
)
def test(given, expected):
    result = strCopies(*given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
