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
    for val in [8,818,8818]:
        print(val, count8(val))


