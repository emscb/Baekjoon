score = []
for i in range(5):
    a = int(input())
    if a < 40:
        score.append(40)
    else:
        score.append(a)
sum = 0
for i in score:
    sum += i
print(int(sum/5))

# Done