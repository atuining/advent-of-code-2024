from collections import Counter

left, right = [], []

with open("2024-1.txt", "r") as f:
    for line in f:
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

left.sort()
right.sort()

sum = 0
for l, r in zip(left, right):
    sum += l - r if l - r >= 0 else r - l

print(sum)

left = set(left)

right = Counter(right)

sum2 = 0

for x in left:
    if x in right:
        sum2 += x * right[x]

print(sum2)
