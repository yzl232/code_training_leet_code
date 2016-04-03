'''
Reverse Words in a String II

given s = "the sky is blue", return "blue is sky the".

Similar to Question [6. Reverse Words in a String], but with the following constraints:
“The input string does not contain leading or trailing spaces and the words are always separated by a single space.”
Could you do it in-place without allocating extra space?


This can be done without any additional space in 2 pass
1) reverse the string in place
2) reverse each word of the reversed string.
'''

class Solution:
    def reverseWords(self, arr):
        self.reverse(arr, 0, len(arr) - 1)
        i = 0
        for j in range(len(arr)):
            if  arr[j] == ' ':
                self.reverse(arr, i, j - 1)
                i = j+1
        self.reverse(arr, i, len(arr) - 1)

    def reverse(self, arr, i, j):
        while i<j:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1;  j-=1


'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        s.reverse()
        index = 0
        for i in range(len(s)):
            if s[i] == " ":
                s[index: i] = reversed(s[index: i])
                index = i + 1
        s[index: ] = reversed(s[index: ])
'''