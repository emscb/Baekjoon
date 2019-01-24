Dial = input()
ans = 0
for i in Dial:
    if ord(i) in [65,66,67]:
        ans += 3
    elif ord(i) in [68,69,70]:
        ans += 4
    elif ord(i) in [71,72,73]:
        ans += 5
    elif ord(i) in [74,75,76]:
        ans += 6
    elif ord(i) in [77,78,79]:
        ans += 7
    elif ord(i) in [80,81,82,83]:
        ans += 8
    elif ord(i) in [84,85,86]:
        ans += 9
    else:
        ans += 10
print(ans)

# Done