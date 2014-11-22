
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
    def findLadders(self, start, end, dict):
        self.start = start
        self.result = []
        self.preMap = {}
        l = len(start)
        for i in dict:
            self.preMap[i] = []
        candidates =set([start])
        while True:
            if len(candidates) == 0:
                return []
            if end in candidates:
                break
            for i in candidates:
                dict.remove(i)   #为甚么放到这里呢？ 想想如果是end, remove掉了， 就影响结果了。
            current = set([])
            for word in candidates:
                for i in range(l):
                    part1 = word[:i]
                    part2 = word[i+1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i] != j:
                            nextword = part1 + j + part2
                            if nextword in dict:
                                self.preMap[nextword].append(word)
                                current.add(nextword)
            candidates = current
        self.buildPath([], end)
        return self.result

    def buildPath(self, path, word):
        if word == self.start:
            temp = path + [word]
            self.result.append(temp[::-1])
            return
        for it in self.preMap[word]:
            self.buildPath(path+[word], it)