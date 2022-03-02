n, k = map(int, input().split())
input()
a = [int(input()) for _ in range(n-1)]
a.reverse()
result = 0
for i in a:
    q, r = divmod(k, i)
    result += q
    k = r
print(result + k)
