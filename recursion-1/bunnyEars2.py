"""
bunnyEars2

We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
(1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say have
3 ears, because they each have a raised foot. Recursively return the number
of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).


bunnyEars2(0) → 0
bunnyEars2(1) → 2
bunnyEars2(2) → 5
"""


def bunnyEars2(bunnies):
    def countEars(bunnies, idx):
        if idx > len(bunnies) - 1:
            return 0

        bunny = bunnies[idx]
        bunnyEars = 3 if bunny % 2 == 0 else 2

        return bunnyEars + countEars(bunnies, idx + 1)

    return countEars(bunnies, 0)


if __name__ == "__main__":
    for val in [list(range(1, 6))]:
        print(val, bunnyEars2(val))
