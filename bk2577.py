A = int(input())
B = int(input())
C = int(input())

ca = A*B*C
Ca = str(ca)[::-1]
D = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
for i in Ca:
    D[i] += 1
for j in D.keys():
    print(D[j])