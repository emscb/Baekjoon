def findJ(A):
    n = A.find("JOI")
    return n


def findI(A):
    n = A.find("IOI")
    return n


A = input()
ansj = 0
ansi = 0

st2 = findJ(A)
st = 0
while(1):
    if st2 == -1:
        break
    else:
        ansj += 1
        st += st2 + 1
        st2 = findJ(A[st:])
print(ansj)

st2 = findI(A)
st = 0
while(1):
    if st2 == -1:
        break
    else:
        ansi += 1
        st += st2 + 1
        st2 = findI(A[st:])
print(ansi)

# Done
