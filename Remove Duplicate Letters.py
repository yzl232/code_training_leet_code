'''
 Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:

Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb" 

'''

class Solution(object):
   def removeDuplicateLetters(self, s): #sort把set自动转换成array了.
        for c in sorted(set(s)):# 贪心.   从最小的ch开始.  如果后面拥有所有的ch, 那么这个chJ就是结果.
            suffix = s[s.index(c):]
            if set(suffix) == set(s):  return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''
'''
 Given the string s, the greedy choice (i.e., the leftmost letter in the answer) is the smallest s[i], s.t. the suffix s[i .. ] contains all the unique letters. (Note that, when there are more than one smallest s[i]'s, we choose the leftmost one. Why? Simply consider the example: "abcacb".)

After determining the greedy choice s[i], we get a new string s' from s by

    removing all letters to the left of s[i],
    removing all s[i]'s from s.

We then recursively solve the problem w.r.t. s'.

The runtime is O(26 * n) = O(n).
'''