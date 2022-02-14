a, b, c = map(int, input().split())
n = int(input())
max_points = 0
for _ in range(n):
    points = 0
    for _ in range(3):
        a0, b0, c0 = map(int, input().split())
        points += a * a0 + b * b0 + c * c0
    if points > max_points:
        max_points = points
print(max_points)