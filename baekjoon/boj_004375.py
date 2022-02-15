import sys
n = sys.stdin.readline()
while n:
    n = int(n)
    n1 = '1'
    while int(n1) % n != 0:
        n1 += '1'
    print(len(n1))
    n = sys.stdin.readline()