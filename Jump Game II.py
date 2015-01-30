'''
 Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
'''

class Solution:
    # @param A, a list of integers
    # @return an integer  #比1只多了几行而已
    def jump(self, arr):
            cnt =0;  lastR=canR = 0   # can reach
            for i in range(len(arr)):
                if i>canR: return -1
                if i > lastR:
                    lastR = canR
                    cnt += 1
                canR = max(canR, i+arr[i])
            return cnt
'''
class Solution
    def jumpGameIII(self, A):
        canReach = False
        if len(A)==1 and int(A[0])!=0:
                canReach = True
                return ', '.join(['0']+['out'])
        maxCanReach = 0;   result = []; lastBig = 0
        for i in range(len(A)):  #O(n)  solution
            if i>maxCanReach: break
            if i>lastBig:
                lastBig = maxCanReach
                if lastPosition<len(A)-1: result.append(str(lastPosition))
                if maxCanReach>=len(A)-1:
                    if maxCanReach==len(A)-1: result.append(str(maxCanReach))
                    canReach=True
                    return ', '.join(result+['out'])
            if int(A[i])+i>maxCanReach:
                maxCanReach = max(int(A[i])+i, maxCanReach)
                lastPosition = i
        if not canReach: return 'failure'

这个是我做project的code





class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        maxCanReach = 0;  jumpNum = 0
        if len(A)<2:  return 0
        while True:
            jumpNum+=1
            for i in range(maxCanReach+1):
                maxCanReach = max(maxCanReach, A[i] + i)
                if maxCanReach >= len(A)-1:   return jumpNum
'''

