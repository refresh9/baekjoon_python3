def solve(n):
    n0 = int(((n * 8 + 1) ** 0.5 - 1) // 2)
    result = n0 * (n0 + 1) * (n0 * 2 + 1) // 6
    n1 = n0 * (n0 + 1) // 2
    result += (n - n1) * (n0 + 1)
    return result

a, b = map(int, input().split())
print(solve(b) - solve(a - 1))