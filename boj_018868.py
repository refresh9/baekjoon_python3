from itertools import combinations
m, n = map(int, input().split())
space = []
for _ in range(m):
    temp1 = list(map(int, input().split()))
    temp2 = dict()
    for i, v in enumerate(sorted(list(set(temp1)))):
        temp2[v] = i
    space.append([temp2[i] for i in temp1])
result = 0
for i, j in combinations(range(m), 2):
    if space[i] == space[j]:
        result += 1
print(result)