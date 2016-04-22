class Solution:
    def reverseWords(self, arr):
        self.reverse(arr, 0, len(arr) - 1)
        i = j = 0
        while j<len(arr):
            while j+1<len(arr) and arr[j+1]!=" ": j+=1
            self.reverse(arr, i, j)
            i = j+2
            j+=1

    def reverse(self, arr, i, j):
        while i<j:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1;  j-=1



'''

#和上面不同。 这个是多个space的情况。 以及边界space的情况
class Solution:  #O(n) space
    def reverseWords(self, s):
        ret = '';   j = len(s)
        for i in range(len(s)-1, -1, -1):
            if s[i]==' ': j=i   #找到了一个可能的结尾
            elif i==0 or s[i-1]==' ':      ret+=s[i:j]+' '   #单词的开始.  意思是现在不是空格。 i-1是空格。 必须加上.  非空格才更新
        return ret[:-1] if ret else ''
s = "the sky is    blue    "
s2 = Solution()
print s2.reverseWords(s)

'''