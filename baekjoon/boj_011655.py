import string
src = input()
dst = ''
orda0, orda1 = ord('A'), ord('a')
for i in src:
    if i in string.ascii_uppercase:
        dst += chr((ord(i) - orda0 + 13) % 26 + orda0)
    elif i in string.ascii_lowercase:
        dst += chr((ord(i) - orda1 + 13) % 26 + orda1)
    else:
        dst += i
print(dst)
