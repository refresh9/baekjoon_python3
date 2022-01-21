sy, sm, sd = map(int, input().split())
ey, em, ed = map(int, input().split())
days = (ey - sy) * 360 + (em - sm) * 30 + (ed - sd)
y0 = days // 360
y = y0 * 15
for i in range(2, y0):
    y += i // 2
m = days // 30
if m > 36:
    m = 36
print(y, m)
print(f'{days}days')