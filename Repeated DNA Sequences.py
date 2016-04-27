'''
 All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].

'''

# 2**20 ;    2**10 = 1k       2**20 = 1 M


class Solution:  # http://www.rudy-yuan.net/archives/148/
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        ret = [];  d = {};  cur = 0
        bit = {'A' : 0b00, 'C' : 0b01, 'G': 0b10, 'T' : 0b11}  # 00, 01, 10, 11
        for i in range(len(s)):
            cur = ((cur << 2) + bit[s[i]]) & 0xFFFFF  #(sum << 2)不加括号会报错.
            if i < 9:    continue
            if cur not in d: d[cur] = 0
            d[cur] += 1
            if d[cur] == 2:  ret.append(s[i - 9 : i + 1])
        return ret

'''
class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        d = {}
        ret = []
        for i in range(len(s)-9):
            t = s[i:i+10]
            if t not in d: d[t] = 0
            d[t] += 1
        return [x for x in d if d[x] > 1]
'''

