'''
This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be calledrepeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two wordsword1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, andword1 and word2 are both in the list.
'''
class WordDistance:
    def __init__(self, words):
        self.d = {}; self.n = len(words)
        for i, w in enumerate(words):
            if w not in self.d:  self.d[w] = []
            self.d[w].append(i)

#一行就可以。不过复杂度不好      return min(abs(i1 - i2) for i1 in self.dic[word1] for i2 in self.dic[word2])
    def shortest(self, w1, w2):
        i = j = 0
        ret = self.n
        while i < len(self.d[w1]) and j < len(self.d[w2]):
            ret = min(ret, abs(self.d[w1][i]-self.d[w2][j]))
            if self.d[w1][i] < self.d[w2][j]:    i += 1
            else:    j += 1
        return ret
# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
