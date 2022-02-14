t = 1
while True:
    n = input()
    if n == '0':
        break
    while True:
        len_n = len(n)
        if len_n % 2 == 1:
            break
        n0 = ''
        for i in range(0, len_n, 2):
            n0 += n[i+1] * int(n[i])
        if n == n0:
            break
        n = n0
    print(f'Test {t}: {n}')
    t += 1