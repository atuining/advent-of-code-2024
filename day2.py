import sys
from time import perf_counter
import threading


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

    def process_chunk(lines, lock):
        nonlocal ans
        local_sum = 0
        for line in lines:
            x = list(map(int, line.split()))
            local_sum += tackle_line(x)
        with lock:
            nonlocal ans
            ans += local_sum

    ans = 0
    lock = threading.Lock()

    with open("2024-2.txt", "r") as f:
        all_lines = f.readlines()

    # Split the work into chunks for different threads
    num_threads = 4  # You can adjust this based on your CPU
    chunk_size = len(all_lines) // num_threads
    threads = []

    start = perf_counter()

    # Create and start threads
    for i in range(num_threads):
        start_idx = i * chunk_size
        end_idx = start_idx + chunk_size if i < num_threads - 1 else len(
            all_lines)
        chunk = all_lines[start_idx:end_idx]

        thread = threading.Thread(target=process_chunk, args=(chunk, lock))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    end = perf_counter()

    print(ans)
    print(f"time = {end - start}")


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
                    return (tackle_line(x, False) or tackle_line(z, False)
                            or tackle_line(w, False))
                else:
                    return False
        return True

    ans = 0

    with open("2024-2.txt", "r") as f:
        for line in f:
            x = list(map(int, line.split()))
            ans += int(tackle_line(x))

    print(ans)


print(sys._is_gil_enabled())
part1()
