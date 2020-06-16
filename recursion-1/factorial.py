def factorial(n):
    if n in (1, 2):
        return n
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    for val in [1,2,3,4,5]:
        print(val, factorial(val))
