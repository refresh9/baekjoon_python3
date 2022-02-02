import sys
n = int(input())
a = list(map(int, input().split()))
if n < 5:
    print(sum(a))
    sys.exit(0)
p = 1
for i in a:
    p *= i
mul = [
    a[-3] * a[-2] * a[-1], a[-2] * a[-1] * a[0],
    a[-1] * a[0] * a[1], a[0] * a[1] * a[2]
]
min_mul = min(mul)
ind = mul.index(min_mul)
p //= min_mul
if ind < 1:
    p += sum(a[-3:])
elif ind < 2:
    p += a[0] + sum(a[-2:])
elif ind < 3:
    p += sum(a[:2]) + a[-1]
else:
    p += sum(a[:3])
print(p)