"""
countX

Given a string, compute recursively (no loops) the number of lowercase 'x' chars
in the string.


countX("xxhixx") → 4
countX("xhixhix") → 3
countX("hi") → 0
"""


def countX(string):
    if not string:
        return 0
    elif len(string) == 1:
        return 1 if string == "x" else 0
    else:
        return countX(string[0]) + countX(string[1:])


if __name__ == "__main__":
    for val in ["xxhixx", "xhixhix", "hi"]:
        print(val, countX(val))
