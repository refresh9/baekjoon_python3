li = list(map(int, input()))
len_li = len(li)
if len_li < 3:
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
else:
    diff = li[1] - li[0]
    for i in range(2, len_li):
        if li[i] - li[i-1] != diff:
            print('흥칫뿡!! <(￣ ﹌ ￣)>')
            break
    else:
        print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')