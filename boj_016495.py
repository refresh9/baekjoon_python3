inp = input()
s = 0
for i in inp:
    s *= 26
    s += ord(i) - ord('A') + 1
print(s)