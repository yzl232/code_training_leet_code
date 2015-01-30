'''
 Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
'''
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for x in tokens:
            if x not in ('+', '-', '*', '/'):  stack.append(int(x))
            else:
                op2 = stack.pop();  op1 = stack.pop()
                if x == '+': stack.append(op1 + op2)
                elif x == '-': stack.append(op1 - op2)
                elif x == '*': stack.append(op1 * op2)
                else: stack.append(int(op1 * 1.0 / op2))
        return stack[0]