birth = list(map(int, list(input())))
n = int(input())
max_biorhythm = 0
max_biorhythm_date = 0
for i in range(n):
    coding_input = input()
    coding = list(map(int, list(coding_input)))
    coding_int = int(coding_input)
    y = (birth[0] - coding[0]) ** 2 + (birth[1] - coding[1]) ** 2
    y += (birth[2] - coding[2]) ** 2 + (birth[3] - coding[3]) ** 2
    m = (birth[4] - coding[4]) ** 2 + (birth[5] - coding[5]) ** 2
    d = (birth[6] - coding[6]) ** 2 + (birth[7] - coding[7]) ** 2
    biorhythm = y * m * d
    if biorhythm > max_biorhythm:
        max_biorhythm = biorhythm
        max_biorhythm_date = coding_int
    elif biorhythm == max_biorhythm:
        if coding_int < max_biorhythm_date:
            max_biorhythm_date = coding_int
print(max_biorhythm_date)