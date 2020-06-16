def count7(n):
    def rec(num):
        if num < 10:
            return 1 if num == 7 else 0
        else:
            rightMostDigit = num % 10
            return rec(rightMostDigit) + rec(num // 10)
    return rec(n)


if __name__ == "__main__":
    for val in [717,7,123]:
        print(val, count7(val))
