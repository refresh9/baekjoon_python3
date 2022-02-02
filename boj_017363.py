n, m = map(int, input().split())
rotate = {
    '-': '|', '|': '-', '\\': '/', '/': '\\',
    '^': '<', '<': 'v', 'v': '>', '>': '^',
    '.': '.', 'O': 'O'
}
picture = ''
for _ in range(n):
    for i in input():
        picture += rotate[i]
for i in range(m-1, -1, -1):
    print(picture[i::m])