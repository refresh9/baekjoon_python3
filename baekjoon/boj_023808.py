n = int(input())
type_a = '@' * n
type_b = type_a + ' ' * (n * 3) + type_a
type_c = type_a * 5
for _ in range(n * 2):
    print(type_b)
for _ in range(n):
    print(type_c)
for _ in range(n):
    print(type_b)
for _ in range(n):
    print(type_c)