import re

N = int(input())
ptrn = input()
ptrn = re.sub("\*", ".*", ptrn)
for _ in range(N):
    st = input()
    ans = re.findall(ptrn, st)
    if ans == []:
        print("NE")
    elif len(st) == len(ans[0]):
        print("DA")
    else: print("NE")

# Done
