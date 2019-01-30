A = input()
ans = ''

for i in A:
    if i == 'A':
        ans += 'X'
    elif i == 'B':
        ans += 'Y'
    elif i == 'C':
        ans += 'Z'
    else:
        ans += chr(ord(i) - 3)
print(ans)

# Done
