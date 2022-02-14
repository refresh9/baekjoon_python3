n = int(input())
a = '@' * (n + 2)
b = '@' + ' ' * n + '@'
print(a)
for _ in range(n):
    print(b)
print(a)