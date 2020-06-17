"""
count8

Given a non-negative int n, compute recursively (no loops) the count of the
occurrences of 8 as a digit, except that an 8 with another 8 immediately to
its left counts double, so 8818 yields 4. Note that mod (%) by 10 yields the
rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost
digit (126 / 10 is 12).


count8(8) → 1
count8(818) → 2
count8(8818) → 4
"""


def count8(n):
    def rec(num, lastVal=None):
        if num < 10:
            curVal = 1 if num == 8 else 0
            if lastVal == 8:
                curVal *= 2
            return curVal
        else:
            rightMostDigit = num % 10
            curSum = rec(rightMostDigit)
            return curSum + rec(num // 10, lastVal=rightMostDigit)

    return rec(n)


if __name__ == "__main__":
    for val in [8, 818, 8818]:
        print(val, count8(val))
