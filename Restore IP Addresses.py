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
        self.ret = []
        self.dfs(0, '', s)
        return self.ret

    def dfs(self, n, cur, s):
        if n == 4:
            if s == '':  self.ret.append(cur[:-1])
            return
        for i in [1, 2, 3]:
            if len(s)>=i:
                ip = s[:i]
                if 0<=int(ip)<=255 and str(int(ip)) == ip:   self.dfs(n+1, cur + ip + '.', s[i:])