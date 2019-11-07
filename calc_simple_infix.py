def calc(a1, a2, op):
    if op == '+':
        return a1 + a2
    elif op == '-':
        return a1 - a2
    elif op == '*':
        return a1 * a2
    elif op == '/':
        return a1 / a2
    elif op == '^':
        return a1 ** a2


while 1:
    A = input()
    if '.' in A:
        try:
            A = float(A)
        except SyntaxError:
            print("Unsupported operand value")
            break
    else:
        try:
            A = int(A)
        except SyntaxError:
            print("Unsupported operand value")
            break
    oprt = input()
    if oprt not in ['+', '-', '*', '/', '^']:
        print("Unsupported operator")
        break
    B = input()
    if '.' in B:
        try:
            B = float(B)
        except SyntaxError:
            print("Unsupported operand value")
            break
    else:
        try:
            B = int(B)
        except SyntaxError:
            print("Unsupported operand value")
            break
    print(calc(A, B, oprt))