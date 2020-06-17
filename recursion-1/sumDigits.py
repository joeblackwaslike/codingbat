"""
sumDigits

Given a non-negative int n, return the sum of its digits recursively
(no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).


sumDigits(126) → 9
sumDigits(49) → 13
sumDigits(12) → 3
"""


def sumDigits(n):
    if n < 10:
        return n
    else:
        rightMostDigit = n % 10
        return rightMostDigit + sumDigits(n // 10)


if __name__ == "__main__":
    for val in [126, 49, 12]:
        print(val, sumDigits(val))
