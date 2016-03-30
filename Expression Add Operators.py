'''


    Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

    Examples:

    "123", 6 -> ["1+2+3", "1*2*3"] 
    "232", 8 -> ["2*3+2", "2+3*2"]
    "105", 5 -> ["1*0+5","10-5"]
    "00", 0 -> ["0+0", "0-0", "0*0"]
    "3456237490", 9191 -> []



'''

class Solution(object):
    def addOperators(self, s, target):
        self.ret, self.target = [], target
        for i in range(1, len(s)+1):  # prevent "00*" as a number
            if i == 1 or s[0] != "0": # prevent "00*" as a number
                self.dfs(s[:i], int(s[:i]), int(s[:i]), s[i:]) # first number in the string
        return self.ret

    def dfs(self, curS, curN, last, s):
        if not s:
            if curN == self.target:  self.ret.append(curS)
            return
        for i in range(1, len(s)+1):
            x = s[:i]
            if i == 1 or s[0] != "0": # prevent "00*" as a number
                self.dfs(curS + "+" + x, curN + int(x), int(x), s[i:])
                self.dfs(curS + "-" + x, curN - int(x), -int(x), s[i:])
                self.dfs(curS + "*" + x, curN - last + last * int(x), last * int(x), s[i:])