n, r, c = map(int, input().split())
st1 = '.v' * (n // 2)
st2 = 'v.' * (n // 2)
is_n_odd = (n % 2 == 1)
if is_n_odd:
    st1 += '.'
    st2 += 'v'
if (r + c) % 2 == 1:
    for _ in range(n // 2):
        print(st1)
        print(st2)
    if is_n_odd:
        print(st1)
else:
    for _ in range(n // 2):
        print(st2)
        print(st1)
    if is_n_odd:
        print(st2)