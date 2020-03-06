bStart, bEnd, bSaving, aStart, aSaving = list(map(int, input().split()))

bobSaving = (bEnd-bStart)*bSaving
print(aStart + bobSaving//aSaving + 1)
