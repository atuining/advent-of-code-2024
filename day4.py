def add(point1: tuple[int, int], point2: tuple[int, int]) -> tuple[int, int]:
    return (point1[0] + point2[0], point1[1] + point2[1])


def check_within_bounds(full_array: list[list[str]], point: tuple[int, int]) -> bool:
    if point[0] < 0 or point[0] >= len(full_array):
        return False
    if point[1] < 0 or point[1] >= len(full_array[0]):
        return False
    return True


def is_xmas(full_array: list[list[str]], point: tuple[int, int]) -> int:
    count = 0

    maybe = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1), (-1, 1), (1, -1)]

    for adds in maybe:
        newp = add(adds, point)
        if (
            check_within_bounds(full_array, newp)
            and full_array[newp[0]][newp[1]] == "M"
        ):
            newp = add(adds, newp)
            if (
                check_within_bounds(full_array, newp)
                and full_array[newp[0]][newp[1]] == "A"
            ):
                newp = add(adds, newp)
                if (
                    check_within_bounds(full_array, newp)
                    and full_array[newp[0]][newp[1]] == "S"
                ):
                    count += 1
    return count


def is_mas(full_array: list[list[str]], point: tuple[int, int]) -> int:
    r, c = point
    top_left = (r - 1, c - 1)
    top_right = (r - 1, c + 1)
    bot_left = (r + 1, c - 1)
    bot_right = (r + 1, c + 1)

    if (
        check_within_bounds(full_array, top_left)
        and check_within_bounds(full_array, top_right)
        and check_within_bounds(full_array, bot_left)
        and check_within_bounds(full_array, bot_right)
    ):
        val_tl = full_array[top_left[0]][top_left[1]]
        val_tr = full_array[top_right[0]][top_right[1]]
        val_bl = full_array[bot_left[0]][bot_left[1]]
        val_br = full_array[bot_right[0]][bot_right[1]]

        cond1 = val_tl == "S" and val_br == "M"
        cond2 = val_tl == "M" and val_br == "S"
        cond3 = val_tr == "S" and val_bl == "M"
        cond4 = val_tr == "M" and val_bl == "S"

        if (cond1 or cond2) and (cond3 or cond4):
            return 1

    return 0


def part1():
    array = []
    with open("2024-4.txt", "r") as f:
        for line in f:
            array.append(list(line))

    m = len(array)
    n = len(array[0])
    count = 0
    for r in range(m):
        for c in range(n):
            if array[r][c] != "X":
                continue
            count += is_xmas(array, (r, c))
    return count


def part2():
    array = []

    with open("2024-4.txt", "r") as f:
        for line in f:
            array.append(list(line))

    m = len(array)
    n = len(array[0])
    count = 0

    for r in range(m):
        for c in range(n):
            if array[r][c] != "A":
                continue

            count += is_mas(array, (r, c))

    return count


print(part2())
