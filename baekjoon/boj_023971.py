h, w, n, m = map(int, input().split())
hn = (h - 1) // (n + 1) + 1
wm = (w - 1) // (m + 1) + 1
print(hn * wm)