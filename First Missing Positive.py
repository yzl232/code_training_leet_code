'''
 Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''
class Solution: #如果是所有数在0-n，那就用求和相减就可以做。  geeksforgeeks。 这里没有
    # @param A, a list of integers
    # @return an integer  # naive thought:  用hashtable. 然后从1到N看是否在hashtable中。 O(n) space and time
    def firstMissingPositive(self, a):
        n = len(a);  i=0   #理想的情况是1~n的组合.  (这句话是本题的关键)  1<=a[i]<=n   #小于0的忽略。
        while i<n:
            tmp = a[i]-1  #求index  -1
            if 0<=tmp<=n-1 and a[i] != a[tmp]: #小于n+1.不然越界。 # 2种都不等于
                a[i], a[tmp] = a[tmp], a[i]
            else: i+=1
        for i in range(n):
            if a[i] != i+1:     return i+1  #求值 +1
        return n+1