class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for k in range(1, len(strs)):
                if len(strs[k])<=i or ch != strs[k][i]:
                    return strs[0][:i]
        return strs[0]