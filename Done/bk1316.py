def group_letter_check(S):
    letter = []
    letterTF = []
    then = 1
    for i in S:
        if i not in letter:
            letter.append(i)
            letterTF.append(True)
            if len(letterTF) != 1:
                letterTF[letter.index(i)-1] = False
        elif i in letter and letterTF[letter.index(i)] is True:
            pass
        elif i in letter and letterTF[letter.index(i)] is False:
            then = 0; break
    return then

N = int(input())
ans = 0
for i in range(N):
    l = input()
    ans += group_letter_check(l)
print(ans)

# Done