def push(l,n):
    l.append(n)

def pop(l):
    if len(l) == 0:
        print(-1)
    else:
        print(l[-1])
        l.pop()

def size(l):
    print(len(l))

def empty(l):
    if len(l) == 0:
        print(1)
    else:
        print(0)

def top(l):
    if len(l) != 0:
        print(l[-1])
    else:
        print(-1)
def run(text, list):
    func = text.split()[0]
    if func == 'push':
        push(list, int(text.split()[1]))
    elif func == 'pop':
        pop(list)
    elif func == 'top':
        top(list)
    elif func == 'size':
        size(list)
    elif func == 'empty':
        empty(list)

N = int(input())
stack = []
for i in range(N):
    run(input(), stack)

# Done