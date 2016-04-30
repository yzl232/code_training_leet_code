'''

LeetCode: Shortest Word Distance III

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.
For example,

Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "makes", word2 = "coding", return 1. Given word1 = "makes", word2 = "makes", return 3.
Note:

You may assume word1 and word2 are both in the list.
'''

#区别  word1 and word2 can be equal
'''
Shortest Word Distance
Total Accepted: 1754 Total Submissions: 4239 Difficulty: Easy

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

'''

class Solution(object):
    def shortestWordDistance(self, words, w1, w2):
        """
        :type words: List[str]
        :type w1: str
        :type w2: str
        :rtype: int
        """
        pre, ret = None, len(words)
        for i, w in enumerate(words):
            if w in [w1, w2]:
                if pre != None and (words[pre] !=w or w1==w2):  ret = min(ret, i-pre)
                pre = i
        return ret