'''
Write a function to generate the generalized abbreviations of a word.

Example:

Given word = "word", return the following list (order does not matter):

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]


如果能想到每一个字符都有2种可能性: abbr或没有abbr.
以"abc"举例: 有3个letter, 所以是$$2^3 = 8$$.
'''

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        ret = []
        def helper(i, cur, cnt):
            if i == len(word):
                ret.append(cur+str(cnt) if cnt>0 else cur)
                return
            helper(i + 1, cur, cnt + 1)
            helper(i + 1, cur +(str(cnt) if cnt>0 else "") +word[i], 0)
        helper(0, "", 0)
        return ret