aliquot_count = int(input())
aliquots = list(map(int, input().split()))
aliquots.sort()
print(aliquots[0] * aliquots[-1])