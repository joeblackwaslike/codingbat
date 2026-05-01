def printRep(char: str, count: int):
    if count == 1:
        print(char)
    else:
        print(char, end="")
        printRep(char, count - 1)


def wedge(n: int):
    def wedgeRec(n: int, i: int):
        if i == n:
            printRep("#", n)
        else:
            printRep("#", i)
            wedgeRec(n, i + 1)
            printRep("#", i)

    wedgeRec(n, 1)


if __name__ == "__main__":
    wedge(6)
