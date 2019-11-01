import re


def compare(a, b):
    n = 0
    seq = ""
    for i in range(len(a)):
        if a[i] == '-' and b[i] == '-':
            seq += '-'
            continue
        elif a[i] == '-' or b[i] == '-':
            if a[i] == '-':
                seq += b[i]
            else:
                seq += a[i]
        elif a[i] == b[i]:
            n += 1
            seq += a[i]
            continue
        elif n != 0 or (n == 0 and seq != ""):
            return -1, ""
    seq = re.sub("-", "", seq)
    return n, seq


def pairwise(a, b):
    N = len(a) + len(b)
    ans = 0
    seq = ""
    for i in range(N+1-len(a)):
        for j in range(N+1-len(b)):
            A = '-'*i + a + '-'*(N-i-len(a))
            B = '-'*j + b + '-'*(N-j-len(b))
            nseq = compare(A, B)
            # if nseq[0] >= 0:
            #     print("Comparing " + A + " and " + B)
            #     print(str(nseq[0]) + " " + nseq[1])
            if nseq[0] > ans:
                ans = nseq[0]
                seq = nseq[1]
            elif nseq[0] == 0 and ans == 0 and nseq[1] != "":
                ans = nseq[0]
                seq = nseq[1]
    # print("Selected : " + seq + ", " + str(ans) + " matched\n")
    return ans, seq


fragments = []
while 1:
    fragment = input()
    if fragment == '':
        break
    fragments.append(fragment)
while len(fragments) != 1:
    N = 0
    SEQ = ""
    I = 0
    J = 0
    for i in range(len(fragments)):
        for j in range(i+1, len(fragments)):
            n = pairwise(fragments[i], fragments[j])
            if n[0] > N:
                N = n[0]
                I = i
                J = j
                SEQ = n[1]
            elif n[0] == 0 and N == 0 and n[1] != "":
                N = n[0]
                I = i
                J = j
                SEQ = n[1]
    # print("Merging : " + fragments[I] + " and " + fragments[J]+'\n')
    if I > I:
        fragments.pop(I)
        fragments.pop(J)
    else:
        fragments.pop(J)
        fragments.pop(I)
    fragments.append(SEQ)
print(fragments[0])