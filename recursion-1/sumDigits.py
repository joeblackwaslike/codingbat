def sumDigits(n):
    if n < 10:
        return n
    else:
        rightMostDigit = n % 10
        return rightMostDigit + sumDigits(n // 10)


if __name__ == "__main__":
    for val in [126, 49, 12]:
        print(val, sumDigits(val))
