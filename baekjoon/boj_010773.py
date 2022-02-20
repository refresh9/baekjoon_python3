k = int(input())
stack = []
for _ in range(k):
    inp = int(input())
    if inp < 1:
        stack.pop()
    else:
        stack.append(inp)
print(sum(stack))