k = int(input())
for x in range(1, k + 1):
    print('Class', x)
    _, *score = map(int, input().split())
    score.sort()
    largestGap = 0
    for i in range(len(score) - 1):
        largestGap = max(largestGap, score[i+1] - score[i])
    print(f'Max {score[-1]}, Min {score[0]}, Largest gap {largestGap}')
