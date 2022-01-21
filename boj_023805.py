n = int(input())
type_a = '@' * n
type_b = ' ' * n
type_c = type_a * 3
type_d = type_c + type_b + type_a
type_e = type_a + type_b + type_a + type_b + type_a
type_f = type_a + type_b + type_c
for _ in range(n):
    print(type_d)
for _ in range(n * 3):
    print(type_e)
for _ in range(n):
    print(type_f)