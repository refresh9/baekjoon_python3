n = int(input())
type_a = '@' * n
type_b = ' ' * n
type_c = type_a + type_b * 3 + type_a
type_d = type_a + type_b * 2 + type_a
type_e = type_a * 3
for _ in range(n):
    print(type_c)
for _ in range(n):
    print(type_d)
for _ in range(n):
    print(type_e)    
for _ in range(n):
    print(type_d)
for _ in range(n):
    print(type_c)