a, b = map(int, input().split())
s = sq1 = 0
sq0 = 1
for i in range(b):
    sq1 += 1
    if i + 1 >= a:
        s += sq0
    if sq0 <= sq1:
        sq0 += 1
        sq1 = 0
print(s)