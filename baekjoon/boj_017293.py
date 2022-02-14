n = int(input())
for i in range(n, 2, -1):
    print(f'{i} bottles of beer on the wall, {i} bottles of beer.')
    print(f'Take one down and pass it around, {i-1} bottles of beer on the wall.')
    print()
if n > 1:
    print('2 bottles of beer on the wall, 2 bottles of beer.')
    print('Take one down and pass it around, 1 bottle of beer on the wall.')
    print()
print('1 bottle of beer on the wall, 1 bottle of beer.')
print('Take one down and pass it around, no more bottles of beer on the wall.')
print()
print('No more bottles of beer on the wall, no more bottles of beer.')
if n < 2:
    print('Go to the store and buy some more, 1 bottle of beer on the wall.')
else:
    print(f'Go to the store and buy some more, {n} bottles of beer on the wall.')