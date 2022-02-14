n = int(input())
type_b = '@' * n
type_a = type_b * 5
for _ in range(n):
    print(type_a)
for _ in range(n * 3):
    print(type_b)
for _ in range(n):
    print(type_a)