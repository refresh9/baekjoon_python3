n = int(input())
type_b = '@' * n
type_a = type_b * 5
for _ in range(n):
    print(type_a)
for _ in range(n):
    print(type_b)
for _ in range(n):
    print(type_a)
for _ in range(n * 2):
    print(type_b)