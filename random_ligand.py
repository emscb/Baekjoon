from random import *

f = open("decoys.smi", 'r')
f2 = open("저장할 파일명", 'w')
ln = sample(range(1, 5200 + 1), 162)
pos = 0
for m in f.readlines():
    if pos in ln:
        f2.write(m)
    pos += 1

f.close()
f2.close()
