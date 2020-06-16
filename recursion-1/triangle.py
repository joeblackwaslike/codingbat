def triangle(rows):
    if rows < 2:
        return rows
    else:
        return 2 + triangle(rows - 1)


if __name__ == "__main__":
    for val in [1,2,3,4,5]:
        print(val, triangle(val))
