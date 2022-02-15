n = int(input())
students = []
for _ in range(n):
    name, d, m, y = input().split()
    date = int(y) * 10000 + int(m) * 100 + int(d)
    students.append((name, date))
students.sort(key=lambda x: x[1])
print(students[-1][0])
print(students[0][0])