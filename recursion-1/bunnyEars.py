"""
bunnyEars

We have a number of bunnies and each bunny has two big floppy ears. We want to
compute the total number of ears across all the bunnies recursively (without
loops or multiplication).


bunnyEars(0) → 0
bunnyEars(1) → 2
bunnyEars(2) → 4
"""


def bunnyEars(bunnies):
    if bunnies == 0:
        return 0
    elif bunnies == 1:
        return 2
    else:
        return 2 + bunnyEars(bunnies - 1)


if __name__ == "__main__":
    for val in range(1, 6):
        print(val, bunnyEars(val))
