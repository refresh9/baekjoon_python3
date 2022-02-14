n, feeling = map(int, input().split())
good_good, good_bad, bad_good, bad_bad = map(float, input().split())
good = bad = 0
if feeling == 0:
    good = 1
else:
    bad = 1
for _ in range(n):
    good, bad = (
        good * good_good + bad * bad_good,
        good * good_bad + bad * bad_bad
    )
good *= 1000
bad *= 1000
int_good, int_bad = int(good), int(bad)
if good - int_good >= 0.5:
    int_good += 1
if bad - int_bad >= 0.5:
    int_bad += 1
print(int_good)
print(int_bad)