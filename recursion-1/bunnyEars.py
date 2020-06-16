def bunnyEars(bunnies):
    if bunnies == 0:
        return 0
    elif bunnies == 1:
        return 2
    else:
        return 2 + bunnyEars(bunnies - 1)


if __name__ == "__main__":
    for val in [1,2,3,4,5]:
        print(val, bunnyEars(val))
