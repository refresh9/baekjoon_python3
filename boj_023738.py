russian = {
    'A': 'a', 'B': 'v', 'E': 'ye', 'K': 'k',
    'M': 'm', 'H': 'n', 'O': 'o', 'P': 'r',
    'C': 's', 'T': 't', 'Y': 'u', 'X': 'h'
}
inp = input()
result = ''
for i in inp:
    result += russian[i]
print(result)