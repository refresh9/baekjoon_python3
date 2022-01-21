n = int(input())
type_a = '@' * n
type_b = type_a * 5
for _ in range(n * 4):
    print(type_a)
for _ in range(n):
    print(type_b)