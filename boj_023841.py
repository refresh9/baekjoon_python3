n, m = map(int, input().split())
m //= 2
for _ in range(n):
    paint = input()
    paint_a = paint[:m]
    paint_b = paint[m:][::-1]
    paint_c = ''
    for i, j in zip(paint_a, paint_b):
        if i != '.':
            paint_c += i
        elif j != '.':
            paint_c += j
        else:
            paint_c += '.'
    print(paint_c + paint_c[::-1])