"""
strDist

https://codingbat.com/prob/p195413

Given a string and a non-empty substring sub, compute recursively the largest
substring which starts and ends with sub and return its length.


strDist("catcowcat", "cat") → 9
strDist("catcowcat", "cow") → 3
strDist("cccatcowcatxx", "cat") → 9
"""


def strDist(string: str, sub: str) -> int:
    pass


import pytest


@pytest.mark.parametrize(
    "given, expected",
    [
        (("catcowcat", "cat"), 9),
        (("catcowcat", "cow"), 3),
        (("cccatcowcatxx", "cat"), 9),
        (("abccatcowcatcatxyz", "cat"), 12),
        (("xyx", "x"), 3),
        (("xyx", "y"), 1),
        (("xyx", "z"), 0),
        (("z", "z"), 1),
        (("x", "z"), 0),
        (("", "z"), 0),
        (("hiHellohihihi", "hi"), 13),
        (("hiHellohihihi", "hih"), 5),
        (("hiHellohihihi", "o"), 1),
        (("hiHellohihihi", "ll"), 2),
    ],
)
@pytest.mark.parametrize("solution", [strDist])
def test(given, expected, solution):
    result = solution(*given)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
