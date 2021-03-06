'''

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:

"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5

'''
class Solution(object):  #这里的stack是考虑乘除需要的,存数字.   之前的是signs, 考虑括号影响
    def calculate(self, s):
        stack, num, preSign = [], 0, "+"
        for i in range(len(s)):
            if s[i].isdigit():   num = num*10+int(s[i])
            if i == len(s)-1 or s[i] in ("+-*/"):   #遇到非数字的时候, 开始计算.  #别用elif
                if preSign in "-+":    stack.append(num*(-1 if preSign == "-" else 1))
                elif preSign == "*":    stack.append(stack.pop()*num)
                else:  #注意和本轮只计算上一轮的sign.
                    x = stack.pop()
                    stack.append((abs(x)/num) * (-1 if x<0 else 1) )
                preSign = s[i]; num = 0
        return sum(stack)

#特点， 有*， /。  所以需要stack pop之前的数。
# 有preSign。
# stack有多个， 最后求sum。 这是考虑  3*4，   5*6. 可以有很多独立的东西在里面

#stack每个单位来自于一个op+一个num.      
#有点类似expression add operators, 那个是用preNum。 这个用了stack。 一样的， 但是这里用preNum代码没这么短。