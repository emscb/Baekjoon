import math
def one(where, width): # 1,4,7,10 ...
    hom = where//3 + 1
    c = "  *   " * hom
    pc = "%" + str(width) + "s"
    print(pc % c.center(width))


def two(where, width): # 2,5,8,11 ...
    hom = where//3 + 1
    c = " * *  " * hom
    pc = "%" + str(width) + "s"
    print(pc % c.center(width))


def three(where, width): # 3,6,9,12 ...
    hom = where//3 + 1
    c = "***** " * hom
    pc = "%" + str(width) + "s"
    print(pc % c.center(width))


a = int(input()) # Whole line number
width = (5*a/3) + a/3 - 1
width = int(width)
pc = "%" + str(width) + "s"
for l in range(a):
    if l+1 == 1:
        print("*".center(width))
    elif l+1 == 2:
        print("* *".center(width))
    elif l+1 == 3:
        print("*****".center(width))
    elif type(math.log(l/3,2)) == int:  # start of routine
        wh = 5*(2**math.log(l/3,2)) + 2**math.log(l/3,2) - 1  # first whitespaces
        while(wh < 0):
