n = int(input())
dic = dict()
for _ in range(n):
    low, upp = input().split()
    dic[upp] = low
str_a = input()
str_b = ''
s, e = map(int, input().split())
for i in str_a:
    str_b += dic[i]
print(str_b[s-1:e])