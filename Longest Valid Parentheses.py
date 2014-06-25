class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):  # http://leetcodenotes.wordpress.com/2013/10/19/leetcode-longest-valid-parentheses-%E8%BF%99%E7%A7%8D%E6%8B%AC%E5%8F%B7%E7%BB%84%E5%90%88%EF%BC%8C%E6%9C%80%E9%95%BF%E7%9A%84valid%E6%8B%AC%E5%8F%B7%E7%BB%84%E5%90%88%E6%9C%89%E5%A4%9A/
        lenS = len(s); stack = [(-1, ')')]; maxLen = 0# anyway, this one  ) is not valid
        for i in range(lenS):
            if s[i] == ')' and stack[-1][1] == '(':  
                stack.pop()  # stack[-1] means stack top (right most)
                maxLen = max(maxLen, i-stack[-1][0])   # the length of the valid part
            else:
                stack.append((i, s[i]))
        return  maxLen