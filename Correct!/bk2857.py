n = 1
c = 0
for _ in range(5):
    A = input()
    if A.find('FBI') != -1:
        c = 1
        print(n, end=' ')
    n += 1
if c == 0:
    print("HE GOT AWAY!")

# Done
