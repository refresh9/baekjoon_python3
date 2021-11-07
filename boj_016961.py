n = int(input())
tap_guests = []
space_guests = []
stay_days_of_the_longest_stay_guest = 0

for _ in range(366):
    tap_guests.append(0)
    space_guests.append(0)

for _ in range(n):
    c, s, e = input().split()
    s, e = int(s) - 1, int(e)
    if c == 'T':
        for i in range(s, e):
            tap_guests[i] += 1
    else:
        for i in range(s, e):
            space_guests[i] += 1
    stay_days = e - s
    if stay_days > stay_days_of_the_longest_stay_guest:
        stay_days_of_the_longest_stay_guest = stay_days
    
days_when_only_one_guest = 0
max_guests = 0
no_fights_days = 0
max_guests_when_no_fights = 0

for i in range(366):
    guests = tap_guests[i] + space_guests[i]
    if guests > 0:
        days_when_only_one_guest += 1
        if guests > max_guests:
            max_guests = guests
        if tap_guests[i] == space_guests[i]:
            no_fights_days += 1
            if guests > max_guests_when_no_fights:
                max_guests_when_no_fights = guests

print(days_when_only_one_guest)
print(max_guests)
print(no_fights_days)
print(max_guests_when_no_fights)
print(stay_days_of_the_longest_stay_guest)