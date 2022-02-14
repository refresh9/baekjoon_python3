import sys
n, m, k = map(int, input().split())
sum_list = []
for _ in range(n):
    temp_list = []
    s = 0
    for i in map(int, input().split()):
        s += i
        temp_list.append(s)
    sum_list.append(temp_list)
for i, v0 in enumerate(zip(*sum_list)):
    for j, v1 in enumerate(v0):
        if v1 >= k:
            print(j + 1, i + 1)
            sys.exit(0)