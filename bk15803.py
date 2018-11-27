from random import *

def one_dim(a,b,x):
    # y=ax+b
    return a*x+b

x=[]
y=[]
for i in range(3):
    a1, b1 = input().split()
    x.append(int(a1))
    y.append(int(b1))

try:
    a = (y[1]-y[0]) / (x[1]-x[0])
except ZeroDivisionError:
    if x[2] == x[1]:
        print("WHERE IS MY CHICKEN?"); exit()
    else:
        print("WINNER WINNER CHICKEN DINNER!"); exit()

b = y[1]-a*x[1]
if one_dim(a,b,x[2]) == y[2]:
    print("WHERE IS MY CHICKEN?")
else:
    print("WINNER WINNER CHICKEN DINNER!")