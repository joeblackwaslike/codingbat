"""
powerN

Given base and n that are both 1 or more, compute recursively (no loops) the
value of base to the n power, so powerN(3, 2) is 9 (3 squared).


powerN(3, 1) → 3
powerN(3, 2) → 9
powerN(3, 3) → 27
"""


def powerN(base, n):
    if n == 1:
        return base
    else:
        return base * powerN(base, n - 1)


if __name__ == "__main__":
    for base, n in [(3, 1), (3, 2), (3, 3)]:
        print((base, n), powerN(base, n))
