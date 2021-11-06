import sys
n = int(input())
if n < 3:
    print(0)
    sys.exit(0)
x0, y0 = map(int, input().split())
x1, y1 = map(int, input().split())
x = [x0, x1]
y = [y0, y1]
for _ in range(n - 2):
    x2, y2 = map(int, input().split())
    x.append(x2)
    y.append(y2)
    x.sort()
    y.sort()
    del x[1]
    del y[1]
print((x[1] - x[0]) * (y[1] - y[0]))