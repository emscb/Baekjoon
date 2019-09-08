f = "7 8 91 3 19 30"
f2 = f.split()
p = 0

for n in f2:
    n = int(n)
    if n > p:
        p = n
print(p)