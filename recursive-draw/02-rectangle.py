def rectangle(n: int, m: int):
    if n == 1:
        if m == 1:
            print(".")
        else:
            print(".", end="")
            rectangle(1, m - 1)
    else:
        rectangle(1, m)
        rectangle(n - 1, m)


if __name__ == "__main__":
    rectangle(5, 8)
