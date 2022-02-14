import sys
n = int(input())
desk = []
row_prof_and_sung = []
col_prof_and_sung = []
for i in range(n):
    desk_row = list(map(int, input().split()))
    desk.append(desk_row)
    if 2 in desk_row:
        row_prof_and_sung.append(i)
        col_prof_and_sung.append(desk_row.index(2))
    if 5 in desk_row:
        row_prof_and_sung.append(i)
        col_prof_and_sung.append(desk_row.index(5))
r1, r2 = sorted(row_prof_and_sung)
c1, c2 = sorted(col_prof_and_sung)
if (r2 - r1) ** 2 + (c2 - c1) ** 2 < 25:
    print(0)
    sys.exit(0)
r2 += 1
c2 += 1
s = 0
for i in range(r1, r2):
    s += sum(desk[i][c1:c2])
if s >= 10:
    print(1)
else:
    print(0)