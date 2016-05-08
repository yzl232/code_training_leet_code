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
        ret, i, signs =0,  0, [1, 1]   # 第一个数字用掉一个1,  另外一个是底，  signs.append(signs[-1] *  里边   sign[-1]用掉一个+1底
        while i < len(s):  # signs.  1代表+号.  -1 代表-号.
            if s[i].isdigit():
                pre = i
                while i+1 < len(s) and s[i+1].isdigit():   i += 1
                ret += signs.pop() * int(s[pre:i+1])   #这里用了乘号,实际上也就是+1或者-1
            elif s[i] in '+-(': signs.append(signs[-1] * (-1 if s[i] =="-" else 1))  #考虑到括号的存在, 都是这个signs[-1] *
            elif s[i] == ')':   signs.pop()
            i += 1
        return ret
#对付括号, 比较特别,   signs .  stack 存的是1, -1
#解法就是从左到右的计算， 考虑括号的因素， +， - 同时由signs决定。
#每次一个括号， 相当于新的开始， 加上一个最基础的符号。
