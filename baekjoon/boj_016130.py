n = int(input())
orda = ord('A') - 10
for _ in range(n):
    inp = input()
    demerit = leave = 0
    for x in inp:
        r0 = demerit // 10
        if x.isdigit():
            demerit += int(x)
        else:
            demerit += ord(x) - orda
        r1 = demerit // 10
        if r0 < r1:
            if r1 < 4:
                leave += r1
            elif r1 == 4:
                print(f'{leave}(weapon)')
                break
            else:
                print(f'{leave}(09)')
                break
    else:
        print(leave)