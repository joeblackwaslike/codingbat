def fibonacci(n):
    if n in (0, 1):
        return n

    return fibonacci(n - 2) + fibonacci(n - 1)



if __name__ == "__main__":
    for val in range(10):
        print(val, fibonacci(val))
