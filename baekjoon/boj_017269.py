alpha = {
    'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4,
    'F': 3, 'G': 1, 'H': 3, 'I': 1, 'J': 1,
    'K': 3, 'L': 1, 'M': 3, 'N': 2, 'O': 1,
    'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2,
    'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2,
    'Z': 1
}
n, m = map(int, input().split())
a, b = input().split()
name = []
for i, j in zip(a, b):
    name.append(alpha[i])
    name.append(alpha[j])
if n > m:
    m -= n
    for i in a[m:]:
        name.append(alpha[i])
elif n < m:
    n -= m
    for i in b[n:]:
        name.append(alpha[i])
len_name = len(name)
while len_name > 2:
    temp_name = []
    for i in range(len_name - 1):
        temp_name.append((name[i] + name[i+1]) % 10)
    name = temp_name
    len_name -= 1
print(f'{name[0] * 10 + name[1]}%')