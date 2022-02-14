n = int(input())
dots = sorted(list(map(int, input().split())))
a = (n - 1) * 2
ans = 0
for i, v in enumerate(dots):
    ans += (i * 4 - a) * v
print(ans)