import string
alpha = set(string.ascii_lowercase)
s, k = input().split()
s, k = s.lower(), int(k)
check = s[0]
s = s[1:] + '0'
num = 1
password = ''
for i in s:
    if check == i:
        num += 1
        continue
    if check in alpha:
        alpha.remove(check)
        if num >= k:
            password += '1'
        else:
            password += '0'
    check = i
    num = 1
print(password)