n = int(input())
result = 0
time = 30
for _ in range(n):
    chapter = int(input())
    if chapter < time:
        result += 1
        time -= chapter
        continue
    if chapter <= time * 2:
        result += 1
    time = 30
print(result)