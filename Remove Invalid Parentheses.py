'''
 Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:

"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]


'''

'''
 Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:

"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]


'''

class Solution(object):
    def removeInvalidParentheses(self, s):
        cur = set([s]);   # set("")会返回empty set .   set([""])  OK
        while True:
            ret = [s for s in cur if self.isValid(s)]
            if ret:    return ret  #实际上是BFS, pre和cur都在下面这行
            cur = set([x[:i] + x[i+1:] for x in cur for i in range(len(x))])

    def isValid(self, s):
        cnt = 0
        for c in s:
            if c == '(':    cnt += 1
            elif c == ')':   cnt -= 1
            if cnt < 0:    return False
        return cnt == 0

