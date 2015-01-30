# encoding=utf-8
'''

Compare Version Numbers
Total Accepted: 6678 Total Submissions: 45070

Compare two version numbers version1 and version1.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
'''

#["1.1", "1.01.0"]
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a boolean
    def compareVersion(self, v1, v2):
        s1=v1.split('.'); s2=v2.split('.')
        for i in range(max(len(s1), len(s2))):
            t1=int(s1[i]) if i<len(s1) else 0
            t2= int(s2[i]) if i<len(s2) else 0
            if t1<t2: return -1
            if t1>t2: return 1
        return 0