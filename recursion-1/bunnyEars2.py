def bunnyEars2(bunnies):
    def countEars(bunnies, idx):
        if idx > len(bunnies) - 1:
            return 0

        bunny = bunnies[idx]
        bunnyEars = 3 if bunny % 2 == 0 else 2

        return bunnyEars + countEars(bunnies, idx + 1)

    return countEars(bunnies, 0)


if __name__ == "__main__":
    for val in [[1,2,3,4,5]]:
        print(val, bunnyEars2(val))
