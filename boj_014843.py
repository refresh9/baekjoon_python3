n = int(input())
score = 0
for _ in range(n):
    inp = input().split()
    s = float(inp[0])
    a, t, m = map(int, inp[1:])
    score += s * (1 / a + 1) * (m / t + 1)
score /= 4
p = int(input())
r = [float(input()) for _ in range(p)]
r.append(score)
r.sort(reverse=True)
if (r.index(score) + 1) * 100 / (p + 1) <= 15:
    print(f'The total score of Younghoon "The God" is {score:.2f}.')
else:
    print(f'The total score of Younghoon is {score:.2f}.')