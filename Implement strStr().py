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
    def strStr(self, haystack, needle):
        # Hanlde two special cases.
        if needle == "":        return 0
        if haystack == "":      return -1
        lenHaystack = len(haystack)
        lenNeedle = len(needle)
        begin = 0  
        # Compare each substring as long as their length
        # is >= the length of needle
        while lenHaystack - begin >= lenNeedle:
            for index in xrange(lenNeedle):
                if haystack[begin+index] != needle[index]:
                    # Find a different char
                    break
            else:
                # Completely the same
                return begin
            begin += 1
        return -1