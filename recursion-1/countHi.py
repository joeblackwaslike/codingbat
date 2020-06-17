"""
countHi

Given a string, compute recursively (no loops) the number of lowercase 'hi' chars
in the string.


countHi("xxhixx") → 4
countHi("xhixhix") → 3
countHi("hi") → 0
"""


def countHi(string):
    if not string:
        return 0
    elif len(string) == 1:
        return 1 if string == "x" else 0
    else:
        return countHi(string[0]) + countHi(string[1:])


if __name__ == "__main__":
    for val in ["xxhixx", "xhixhix", "hi"]:
        print(val, countHi(val))
