input()
inp = input()
dance = [''] * 5
for i in inp:
    if i == 'o':
        dance[0] += 'o'
        dance[1] += 'w'
        dance[2] += 'l'
        dance[3] += 'n'
        dance[4] += '.'
    elif i == 'w':
        dance[0] += '.'
        dance[1] += 'o'
        dance[2] += 'm'
        dance[3] += 'l'
        dance[4] += 'n'
    else:
        dance[0] += '.'
        dance[1] += '.'
        dance[2] += 'o'
        dance[3] += 'L'
        dance[4] += 'n'
print(*dance, sep='\n')