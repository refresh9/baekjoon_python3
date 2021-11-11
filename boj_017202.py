a = input()
b = input()
ab = ''
for i in range(8):
    ab += a[i] + b[i]
ab = list(map(int, ab))
for _ in range(14):
    ab0 = []
    for i in range(len(ab) - 1):
        ab0.append((ab[i] + ab[i+1]) % 10)
    ab = ab0
print(ab[0], ab[1], sep='')