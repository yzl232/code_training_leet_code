class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs)==0: return ''
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if len(strs[j])<i+1 or strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]