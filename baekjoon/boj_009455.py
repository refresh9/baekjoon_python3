t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    box_sum_col = [0] * n
    result = 0
    for i in range(m):
        box_row = list(map(int, input().split()))
        dist_row = m - i - 1
        for j, v in enumerate(box_row):
            if v > 0:
                result += dist_row
                box_sum_col[j] += 1
    for i in box_sum_col:
        result -= i * (i - 1) // 2
    print(result)