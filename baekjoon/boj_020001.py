problem = 0
input()
inp = input()
while inp != '고무오리 디버깅 끝':
    if inp == '문제':
        problem += 1
    elif inp == '고무오리':
        if problem > 0:
            problem -= 1
        else:
            problem = 2
    inp = input()
if problem > 0:
    print('힝구')
else:
    print('고무오리야 사랑해')