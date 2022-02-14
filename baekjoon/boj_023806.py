n = int(input())
type_a = '@' * n
type_b = type_a * 5
type_c = type_a + ' ' * (n * 3) + type_a
for _ in range(n):
    print(type_b)
for _ in range(n * 3):
    print(type_c)
for _ in range(n):
    print(type_b)