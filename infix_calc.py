class Stack:
    def __init__(self):
        self.data = []
        self.top = -1

    def push(self, n):
        self.data.append(n)
        self.top += 1

    def pop(self):
        N = self.data[self.top]
        del self.data[self.top]
        self.top -= 1
        return N

    def view(self):
        return self.data[self.top]

    def is_empty(self):
        return self.top == -1


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


error_code = 0
while 1:
    A = input()
    oprn = Stack()
    oprt = Stack()
    is_oprn = False
    is_float = False
    is_start_of_parenthesis = False
    tmp_oprn = ""
    before_oprn = ""
    error_code = 0

    for a in A:
        if '0' <= a <= '9':
            if is_oprn:
                tmp_oprn += a
            elif before_oprn == ')':
                print("Error : Digit next to right parenthesis")
                error_code = -1
                break
            else:
                is_oprn = True
                tmp_oprn += a
        elif a in ['*', '/']:
            if before_oprn == '.':
                print("Error : Invalid float operand")
                error_code = -1
                break
            if is_oprn:
                oprn.push(float(tmp_oprn) if is_float else int(tmp_oprn))
                tmp_oprn = ""
            if is_oprn or before_oprn == ')':
                if not oprt.is_empty() and oprt.view() in ['*', '/', '^']:
                    a2 = oprn.pop()
                    a1 = oprn.pop()
                    op = oprt.pop()
                    oprn.push(calc(a1, a2, op))
                    oprt.push(a)
                else:
                    oprt.push(a)
            else:
                print("Error : Operator duplicated")
                error_code = -1
                break
            is_oprn = False
            is_float = False
        elif a in ['+', '-']:
            if before_oprn == '.':
                print("Error : Invalid float operand")
                error_code = -1
                break
            if is_oprn:
                oprn.push(float(tmp_oprn) if is_float else int(tmp_oprn))
                tmp_oprn = ""
            if is_oprn or before_oprn == ')':
                if oprt.is_empty() or oprt.view() == '(':
                    oprt.push(a)
                else:
                    a2 = oprn.pop()
                    a1 = oprn.pop()
                    op = oprt.pop()
                    oprn.push(calc(a1, a2, op))
                    oprt.push(a)
            elif before_oprn == '(':
                oprn.push(0)
                oprt.push(a)
            else:
                print("Error : Operator duplicated")
                error_code = -1
                break
            is_oprn = False
            is_float = False
        elif a == '(':
            if before_oprn == '.':
                print("Error : Invalid float operand")
                error_code = -1
                break
            if is_oprn:
                print("Error : There is not operator next to operand")
                error_code = -1
                break
            elif before_oprn == ')':
                print("Error : There is not operator between parenthesis")
                error_code = -1
                break
            else:
                oprt.push(a)
                is_start_of_parenthesis = True
        elif a == ')':
            if before_oprn == '.':
                print("Error : Invalid float operand")
                error_code = -1
                break
            if not is_start_of_parenthesis:
                print("Error : Parenthesis not opened")
                error_code = -1
                break
            if is_oprn:
                is_oprn = False
                oprn.push(float(tmp_oprn) if is_float else int(tmp_oprn))
                is_float = False
                tmp_oprn = ""
            else:
                print("Error : There is not operand before right parenthesis")
                error_code = -1
                break
            while oprt.view() != '(':
                a2 = oprn.pop()
                a1 = oprn.pop()
                op = oprt.pop()
                oprn.push(calc(a1, a2, op))
            oprt.pop()
            is_start_of_parenthesis = False
        elif a == '^':
            if before_oprn == '.':
                print("Error : Invalid float operand")
                error_code = -1
                break
            if is_oprn:
                is_oprn = False
                oprn.push(float(tmp_oprn) if is_float else int(tmp_oprn))
                is_float = False
                tmp_oprn = ""
            else:
                print("Error : Operator duplicated")
                error_code = -1
                break
            oprt.push(a)
        elif a == '.':
            if is_float:
                print("Error : Invalid float operand")
                error_code = -1
                break
            if is_oprn:
                is_float = True
                tmp_oprn += a
            elif before_oprn == ')':
                print("Error : There is not operator next to right parenthesis")
            else:
                is_float = True
                is_oprn = True
                tmp_oprn += '0.'
        else:
            print("Error : Not supported operator")
            error_code = -1
            break
        before_oprn = a
    if error_code != 0:
        continue
    if is_oprn:
        is_oprn = False
        oprn.push(float(tmp_oprn) if is_float else int(tmp_oprn))
        is_float = False
        tmp_oprn = ""
    while oprn.top != -1:
        a2 = oprn.pop()
        a1 = oprn.pop()
        op = oprt.pop()
        oprn.push(calc(a1, a2, op))
    print(oprn.pop()) if oprt.is_empty() else print("Error : Operand missed")
    del oprn
    del oprt
