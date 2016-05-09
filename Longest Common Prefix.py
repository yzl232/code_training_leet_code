#Write a function to find the longest common prefix string amongst an array of strings.
class Solution:
    # @return a string
    def longestCommonPrefix(self, arr):
        if not arr: return ''
        for i, ch in enumerate(arr[0]):
            for s in arr[1:]:
                if not (i<len(s) and ch==s[i]):    return arr[0][:i]
        return arr[0]
# 可以这样子。 先写 if        or s[i]!=arr[0][i]:。   再填充上去。