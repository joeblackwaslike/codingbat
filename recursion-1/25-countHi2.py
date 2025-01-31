"""
countHi2

https://codingbat.com/prob/p143900

Given a string, compute recursively the number of times lowercase "hi" appears
in the string, however do not count "hi" that have an 'x' immedately before
them.


countHi2("ahixhi") → 1
countHi2("ahibhi") → 2
countHi2("xhixhi") → 0
"""


def countHi2(string: str) -> int:
    pass


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        ("ahixhi", 1),
        ("ahibhi", 2),
        ("xhixhi", 0),
        ("hixhi", 1),
        ("hixhhi", 2),
        ("hihihi", 3),
        ("hihihix", 3),
        ("xhihihix", 2),
        ("xxhi", 0),
        ("hixxhi", 1),
        ("hi", 1),
        ("xxxx", 0),
        ("h", 0),
        ("x", 0),
        ("", 0),
        ("Hellohi", 1),
    ],
)
def test(given, expected):
    result = countHi2(given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
