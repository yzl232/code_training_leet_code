
'''
 Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:

    Only one letter can be changed at a time
    Each intermediate word must exist in the dictionary

For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]

Return

  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]

Note:

    All words have the same length.
    All words contain only lowercase alphabetic characters.

'''

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def dfs(self, path):
        if path[-1]==self.start:  #start
            self.ret.append(path[::-1])
            return
        for x in self.preW[path[-1]]:
            self.dfs(path+[x])

    def findLadders(self, start, end, dict):
        self.ret, self.preW, pre = [], {x: [] for x in dict}, set([start]);  self.start=start
        while pre and end not in pre:
            for w in pre:   dict.remove(w)   #为甚么放到这里呢？ 如果是end, remove掉了， 就影响结果了。
            cur = set()
            for w in pre:
                for i in range(len(w)):
                    for x in 'abcdefghijklmnopqrstuvwxyz':
                        c = w[:i] + x + w[i + 1:]
                        if c in dict:
                            self.preW[c].append(w)
                            cur.add(c)
            pre = cur
        if pre:    self.dfs([end])  # end in pre.
        return self.ret