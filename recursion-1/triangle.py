"""
triangle

We have triangle made of blocks. The topmost row has 1 block, the next row down
has 2 blocks, the next row has 3 blocks, and so on. Compute recursively (no
loops or multiplication) the total number of blocks in such a triangle with the
given number of rows.


triangle(0) → 0
triangle(1) → 1
triangle(2) → 3
"""


def triangle(rows):
    if rows < 2:
        return rows
    else:
        return 2 + triangle(rows - 1)


if __name__ == "__main__":
    for val in range(1, 6):
        print(val, triangle(val))
