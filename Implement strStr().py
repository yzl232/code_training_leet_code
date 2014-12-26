'''
 Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Update (2014-11-02):
The signature of the function had been updated to return the index instead of the pointer. If you still see your function signature returns a char * or String, please click the reload button to reset your code definition.
'''
class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, s, s1):
        if s1 == "":        return 0
        if s == "":      return -1
        m = len(s);  n = len(s1);   i = 0
        while m - i >= n:
            for j in range(n):
                if s[i+j] != s1[j]:    break
            else:    return i
            i += 1
        return -1