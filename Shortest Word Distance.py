'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list. 
'''
class Solution:
    def shortestDistance(self, words, w1, w2):
        pre, ret = None, len(words)
        for i, x in enumerate(words):
            if x in [w1, w2]:
                if pre != None and (words[pre] != x): ret = min(ret, i-pre)   
                pre = i   # if current matched word is different from last matched word
        return ret


#类似题目    Find Index of 0 to be replaced with 1 to get longest continuous sequence of 1s in a binary array


#为了与三保持一致, 改用一个pointer
'''
class Solution(object):
    def shortestDistance(self, words, word1, word2):# one pass
        p1 = p2 = -1; ret = len(words)+1
        for i in range(len(words)):
            if words[i] == word1:  p1 = i
            if words[i] == word2: p2 = i
            if p1!= -1 and p2!=-1:  ret = min(ret, abs(p1-p2))
        return ret


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        return min(abs(i - j) for i in xrange(len(words)) if words[i] == word1 for j in xrange(len(words)) if words[j] == word2)
'''


'''
#geeks做过。   
Find the minimum distance between two numbers
'''