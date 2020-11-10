# 5분 빠른 경우

import re


def print_int(i):
    if i > 9:
        return str(i)
    else:
        return "0" + str(i)


content = open('timing.txt', 'r')
newContent = open('timing_edited.txt', 'w')
newLine = ""
for c in content.readlines():
    if c == "\n":
        newLine += "\n"
    elif len(c) <= 3:
        newLine += c
        print(c)
    else:
        exp = re.compile(r"(\d{2}):(\d{2}):(\d{2}).(\d{3})\s+-->\s+(\d{2}):(\d{2}):(\d{2}).(\d{3})")
        fa2 = re.findall(exp, c)
        if len(fa2) == 0:
            newLine += c
            continue
        fa = re.search(exp, c)
        a1, a2, a3, a4, a5, a6, a7, a8 = fa.groups()
        a1 = int(a1)
        a2 = int(a2)
        a3 = int(a3)
        a5 = int(a5)
        a6 = int(a6)
        a7 = int(a7)

        if a3 + 5 >= 60:
            if a2 + 1 >= 60:
                newLine += print_int(a1 + 1) + ":" + print_int(a2 + 1 - 60) + ":" + print_int(a3 + 5 - 60) + "," + a4
            else:
                newLine += print_int(a1) + ":" + print_int(a2 + 1) + ":" + print_int(a3 + 5 - 60) + "," + a4
        else:
            newLine += print_int(a1) + ":" + print_int(a2) + ":" + print_int(a3 + 5) + "," + a4

        newLine += " --> "

        if a7 + 5 >= 60:
            if a6 + 1 >= 60:
                newLine += print_int(a5 + 1) + ":" + print_int(a6 + 1 - 60) + ":" + print_int(
                    a7 + 5 - 60) + "," + a8 + "\n"
            else:
                newLine += print_int(a5) + ":" + print_int(a6 + 1) + ":" + print_int(a7 + 5 - 60) + "," + a8 + "\n"
        else:
            newLine += print_int(a5) + ":" + print_int(a6) + ":" + print_int(a7 + 5) + "," + a8 + "\n"

# print(newLine)
newContent.write(newLine)
