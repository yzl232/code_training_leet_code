class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        # Hanlde two special cases.
        if needle == "":        return haystack
        if haystack == "":      return None
        
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
                return haystack[begin:]
            
            begin += 1
        
        return None