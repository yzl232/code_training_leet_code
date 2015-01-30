
'''
 Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column..
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, arr):
        n = len(arr) #举个例子就容易写。 687432   =》  找到 6， 和7交换。  =》786432=>723468
        for i in range(n-1, 0, -1):
            if arr[i]>arr[i-1]:
                for j in range(n-1, i-1, -1):  #背过中间四行就好
                    if arr[j]>arr[i-1]: break
                arr[j], arr[i-1] = arr[i-1], arr[j]
                l = i; r = n-1
                while l<r:
                    arr[l], arr[r] = arr[r], arr[l]
                    l+=1; r-=1
                return arr
        arr.reverse()
        return arr     #是O(n)的 #http://blog.csdn.net/m6830098/article/details/17291259
