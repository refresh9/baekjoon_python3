r, c = map(int, input().split())
feed = [[0] * c for _ in range(r)]
for i in range(c):
    tmp = list(map(int, input().split()))
    for j, v in enumerate(tmp):
        feed[j][-i-1] = v

wink = True
for i in range(r):
    tmp = list(map(int, input().split()))
    if tmp != feed[i]:
        wink = False
        break

if wink:
    print('|>___/|        /}')
    print('| O < |       / }')
    print('(==0==)------/ }')
    print('| ^  _____    |')
    print('|_|_/     ||__|')
else:
    print('|>___/|     /}')
    print('| O O |    / }')
    print('( =0= )""""  \\')
    print('| ^  ____    |')
    print('|_|_/    ||__|')