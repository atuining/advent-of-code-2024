def part1():
    def tackle_line(x: list[int]) -> bool:
        if len(x) < 2:
            return True
        sign = x[1] > x[0]
        for i, y in enumerate(x[1:]):
            t = y - x[i]
            if ((t > 0) != sign) or abs(t) < 1 or abs(t) > 3:
                return False
        return True

    ans = 0
    with open("2024-2.txt", "r") as f:
        for line in f:
            x = line.split()
            x = list(map(int, x))
            ans += int(tackle_line(x))

    print(ans)


def part2():
    def tackle_line(x: list[int], try_again: bool = True) -> bool:
        if len(x) < 2:
            return True
        sign = x[1] > x[0]
        for i, y in enumerate(x[1:]):
            t = y - x[i]
            if ((t > 0) != sign) or abs(t) < 1 or abs(t) > 3:
                if try_again:
                    z = x.copy()
                    w = x.copy()
                    del x[i]
                    del z[i + 1]
                    del w[i - 1]
                    return (
                        tackle_line(x, False)
                        or tackle_line(z, False)
                        or tackle_line(w, False)
                    )
                else:
                    return False
        return True

    ans = 0

    with open("2024-2.txt", "r") as f:
        for line in f:
            x = list(map(int, line.split()))
            ans += int(tackle_line(x))

    print(ans)


part2()
