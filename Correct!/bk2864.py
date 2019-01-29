AB = input()
A, B = AB.split()[0], AB.split()[1]

Am = A.replace('6', '5')
Bm = B.replace('6', '5')

AM = A.replace('5', '6')
BM = B.replace('5', '6')

m = int(Am) + int(Bm)
M = int(AM) + int(BM)

print(m, M)

# Done
