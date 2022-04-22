n = int(input())
if n < 5:
    print(0)
else:
    zero = 1
    for i in range(10, n + 1):
        while i % 5 == 0:
            zero += 1
            i //= 5
    print(zero)
