n = int(input())
a = list(map(int, input().split()))
x, y = map(int, input().split())
relative = n * x // 100
a.append(y)
a.sort()
absolute = n - a.index(y)
print(relative, absolute)