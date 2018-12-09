a = input().split()
A = a[0][::-1]
B = a[1][::-1]
A = int(A)
B = int(B)
if A > B:
    print(A)
else:
    print(B)

# Done