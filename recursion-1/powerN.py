def powerN(base, n):
    if n == 1:
        return base
    else:
        return base * powerN(base, n - 1)


if __name__ == "__main__":
    for base, n in [(3, 1), (3, 2), (3, 3)]:
        print((base, n), powerN(base, n))
