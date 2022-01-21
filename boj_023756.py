n = int(input())
a0 = int(input())
s = 0
for _ in range(n):
    a1 = int(input())
    a2, a3 = sorted([a0, a1])
    s += min(a3 - a2, a2 + 360 - a3)
    a0 = a1
print(s)