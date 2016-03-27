'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:

"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23

'''

class Solution(object):
    def calculate(self, s):
        total = 0
        i, signs = 0, [1, 1]   # 第一个数字用掉一个1,  另外signs.append(signs[-1] * (-1 if c=="-" else 1))用掉一个1
        while i < len(s):  # signs.  1代表+号.  -1 代表-号.
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():   i += 1
                total += signs.pop() * int(s[start:i])   #这里用了乘号,实际上也就是+1或者-1
                continue
            if c in '+-(': signs.append(signs[-1] * (-1 if c=="-" else 1))  #考虑到括号的存在, 都是这个signs[-1] *
            elif c == ')':   signs.pop()
            i += 1
        return total
