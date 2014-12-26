'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''
class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        self.result = []
        self.dfs(0, '', s)
        return self.result

    def dfs(self, num, cur, s):
        if num == 4:
            if s == '':  self.result.append(cur[:-1])
            return
        for i in range(1, 4):
            if len(s)>=i:
                ip = s[:i]
                if 0<=int(ip)<=255 and str(int(ip)) == ip:
                    self.dfs(num+1, cur + ip + '.', s[i:])