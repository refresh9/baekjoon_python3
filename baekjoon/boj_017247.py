n, m = map(int, input().split())
xy = []
num1 = 0
for x in range(n):
    inp = input()
    y0 = inp.find('1')
    if y0 >= 0:
        num1 += 1
        xy.append((x, y0 // 2))
        if num1 > 1:
            break
        y1 = inp[y0+2:].find('1')
        if y1 >= 0:
            xy.append((x, (y0 + y1 + 2) // 2))
            break
d = abs(xy[1][0] - xy[0][0]) + abs(xy[1][1] - xy[0][1])
print(d)