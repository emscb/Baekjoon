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
    A = input("Infix statement : ")
    oprt = Stack()
    is_oprn = False
    is_start_of_parenthesis = False
    tmp_oprn = ""
    before_oprn = ""
    postfix = ""

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
                postfix += tmp_oprn + " "
                tmp_oprn = ""
            if is_oprn or before_oprn == ')':
                if not oprt.is_empty() and oprt.view() in ['*', '/', '^']:
                    postfix += oprt.pop() + " "
                    oprt.push(a)
                else:
                    oprt.push(a)
            else:
                print("Error : Operator duplicated")
                error_code = -1
                break
            is_oprn = False
        elif a in ['+', '-']:
            if before_oprn == '.':
                print("Error : Invalid float operand")
                error_code = -1
                break
            if is_oprn:
                postfix += tmp_oprn + " "
                tmp_oprn = ""
            if is_oprn or before_oprn == ')':
                if oprt.is_empty() or oprt.view() == '(':
                    oprt.push(a)
                else:
                    postfix += oprt.pop() + " "
                    oprt.push(a)
            elif before_oprn == '(' and a == '-':
                postfix += '-'
            else:
                print("Error : Operator duplicated")
                error_code = -1
                break
            is_oprn = False
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
                postfix += tmp_oprn + " "
                tmp_oprn = ""
            else:
                print("Error : There is not operand before right parenthesis")
                error_code = -1
                break
            # Todo 왼괄호가 나올 때 까지 다 꺼내기
