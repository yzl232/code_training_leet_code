'''
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this new language.Derive the order of letters in this language.

For example,
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

The correct order is: "wertf".

Note:

    You may assume all letters are in lowercase.
    If the order is invalid, return an empty string.
    There may be multiple valid order of letters, return any one of them is fine.
'''




class Solution:  # build graph有技巧。 必须相邻比较words.
    def topolgical_sort(self, words):
        g = {}
        for ch in set(''.join(words)):  g[ch] = set()    #第一步： 为所有的ch建立node
        for i in range(len(words)-1):
            w1 = words[i]; w2 = words[i+1]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:  #发现了一个edge,  加入graph
                    g[w2[j]].add(w1[j]);   break
        print g
        self.graph = g
        self.ret,  self.visited = [], {}
        for k in g:  self.dfs(k)
        return self.ret

    def dfs(self, x):
        if x in self.visited:   #已经visit过了
            if self.visited[x]==False: raise ValueError("cycle")  #发现了一个back edge。
            return
        self.visited[x] = False  #这就是与普通dfs的唯一不同。 用False标记
        for k in self.graph[x]:  self.dfs(k)
        self.ret.append(x)
        self.visited[x] = True

s = Solution()
print s.topolgical_sort(["baa", "abcd", "abca", "cab", "cad"])
print s.topolgical_sort(["caa", "aaa", "aab"])
