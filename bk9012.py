def push(l):
    l.append(1)

def pop(l):
    if len(l) == 0:
        l.append(-1)
    elif l[0] == -1:
        l.append(-1)
    else:
        l.pop()

T = int(input())

for i in range(T):
    stk = []
    qus=input()
    for k in qus:
        if k == '(':
            push(stk)
        elif k == ')':
            pop(stk)
    if len(stk) == 0:
        print("YES")

    elif stk[0] == -1:
        print("NO")

    else: print("NO")
