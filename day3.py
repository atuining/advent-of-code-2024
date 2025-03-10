import re
def part1():
    answer = 0
    with open("2024-3.txt", 'r') as f:
        for line in f:
            r = re.compile(r'mul\([0-9]+,[0-9]+\)')
            line = r.findall(line)
            for fun in line:
                r = re.compile('[0-9]+')
                fun = r.findall(fun)
                answer += int(fun[0]) * int(fun[1])
    return answer

def part2():
    answer = 0
    with open("2024-3.txt", 'r') as f:
        do = True
        for line in f:
            r = re.compile(r"don't|mul\([0-9]+,[0-9]+\)|do")
            line = r.findall(line)
            for fun in line:
                if fun == "do":
                    do = True
                elif fun == "don't":
                    do = False
                elif do == True:
                    r = re.compile(r'\d+')
                    fun = r.findall(fun)
                    answer += int(fun[0]) * int(fun[1])
    return answer

print(part2())
