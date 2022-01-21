k, n = map(int, input().split())
if n < 2:
    print(-1)
else:
    x = k * n // (n - 1)
    while (x - k) * n < x:
        x += 1
    print(x)