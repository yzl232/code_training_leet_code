'''

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:

"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5

'''
class Solution(object):
    def calculate(self, s):
        stack, num, sign = [], 0, "+"
        for i in range(len(s)):
            if s[i].isdigit():   num = num*10+int(s[i])
            if i == len(s)-1 or s[i] in ("+-*/"):   #遇到非数字的时候, 开始计算.
                if sign == "-":    stack.append(-num)
                elif sign == "+":    stack.append(num)
                elif sign == "*":    stack.append(stack.pop()*num)
                else:
                    x = stack.pop()
                    stack.append((abs(x)/num) * (-1 if x<0 else 1) )
                sign = s[i]
                num = 0
        return sum(stack)