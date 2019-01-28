for _ in range(3):
    A = input().split()
    a = 0
    for i in A:
        if i == '0':
            a += 1
    if a == 0:
        print("E")
    elif a == 1:
        print("A")
    elif a == 2:
        print("B")
    elif a == 3:
        print("C")
    elif a == 4:
        print("D")

# Done
