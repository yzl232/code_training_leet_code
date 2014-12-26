
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
    def dfs(self, path, word):
        if not self.preW[word]:  #start
            self.ret.append(path[::-1])
            return
        for prev in self.preW[word]:
            self.dfs(path+[prev], prev)

    def findLadders(self, start, end, dict):
        self.ret, self.preW, pre = [], {word: [] for word in dict}, set([start])
        while pre and end not in pre:
            for word in pre:   dict.remove(word)   #为甚么放到这里呢？ 如果是end, remove掉了， 就影响结果了。
            cur = set([])
            for word in pre:
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        c = word[:i] + j + word[i + 1:]
                        if c in dict:
                            self.preW[c].append(word)
                            cur.add(c)
            pre = cur
        if pre:    self.dfs([end], end)
        return self.ret