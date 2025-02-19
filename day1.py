from collections import Counter

left: list[int] = []
right: list[int] = []

with open("2024-1.txt", "r") as f:
    for line in f:
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

left.sort()
right.sort()

sum3 = 0
for l, r in zip(left, right):
    sum3 += l - r if l - r >= 0 else r - l

print(sum3)

leftset = set(left)

rightmap = Counter(right)

sum2 = 0

for x in leftset:
    if x in rightmap:
        sum2 += x * rightmap[x]

print(sum2)

similarity = 0

for element in left:
    similarity += element * sum(1 for n in right if n == element)

print(f"{similarity=}")
