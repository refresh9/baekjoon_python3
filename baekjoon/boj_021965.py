n = int(input())
a = list(map(int, input().split()))
up = True
for i in range(n - 1):
    if up:
        if a[i] < a[i+1]:
            continue
        else:
            up = False
    if not up:
        if a[i] > a[i+1]:
            continue
        else:
            print('NO')
            break
else:
    print('YES')