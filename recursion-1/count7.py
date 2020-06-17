"""
count7

Given a non-negative int n, return the count of the occurrences of 7 as a
digit, so for example 717 yields 2. (no loops). Note that mod (%) by 10 yields
the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the
rightmost digit (126 / 10 is 12).


count7(717) → 2
count7(7) → 1
count7(123) → 0
"""


def count7(n):
    def rec(num):
        if num < 10:
            return 1 if num == 7 else 0
        else:
            rightMostDigit = num % 10
            return rec(rightMostDigit) + rec(num // 10)

    return rec(n)


if __name__ == "__main__":
    for val in [717, 7, 123]:
        print(val, count7(val))
