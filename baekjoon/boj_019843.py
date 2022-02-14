t, n = map(int, input().split())
days = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4}
t_sum = 0
for _ in range(n):
    d1, h1, d2, h2 = input().split()
    t1 = days[d1] * 24 + int(h1)
    t2 = days[d2] * 24 + int(h2)
    t_sum += t2 - t1
t -= t_sum
if t > 48:
    print(-1)
elif t <= 0:
    print(0)
else:
    print(t)