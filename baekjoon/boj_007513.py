t = int(input())
for i in range(1, t+1):
    print(f'Scenario #{i}:')
    m = int(input())
    words = [input() for _ in range(m)]
    n = int(input())
    for _ in range(n):
        k, *index = map(int, input().split())
        password = ''
        for j in index:
            password += words[j]
        print(password)
    print()