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
class Solution:
    def __init__(self, words):
        self.d, self.n = {}, len(words)
        for i, w in enumerate(words):
            if w not in self.d: self.d[w] = []
            self.d[w].append(i)
    
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    # Adds a word into the data structure.
    def shortest(self, word1, word2):
        arr1, arr2 = self.d[word1], self.d[word2]
        i = j = 0
        ret = self.n
        while i < len(arr1) and j < len(arr2):
            ret = min(ret, abs(arr1[i]-arr2[j]))
            if arr1[i] < arr2[j]:    i += 1
            else:    j += 1
        return ret
        # O(m+n) time complexity
