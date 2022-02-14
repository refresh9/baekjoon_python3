import math
x, y, p1, p2 = map(int, input().split())
gcd = math.gcd(x, y)
if p1 % gcd == p2 % gcd:
    if p1 > p2:
        x, y, p1, p2 = y, x, p2, p1
    r = p1 % x
    result = p2
    while result % x != r:
        result += y
    print(result)
else:
    print(-1)