t = int(input())
for _ in range(t):
    x = list(map(int, input().split()))
    card = []
    for i, v in enumerate(x):
        if i == 5:
            for _ in range(v):
                card.append(9)
        else:
            for _ in range(v):
                card.append(i+1)
    card.sort()
    n = len(card) % 2
    card = card[-1::-2] + card[n::2]
    print(*card)