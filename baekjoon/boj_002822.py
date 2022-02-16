score = [int(input()) for _ in range(8)]
score = list(enumerate(score))
score = sorted(score, key=lambda x: x[1], reverse=True)
quiz = []
sum_score = 0
for i, j in score[:5]:
    quiz.append(i + 1)
    sum_score += j
print(sum_score)
print(*sorted(quiz))