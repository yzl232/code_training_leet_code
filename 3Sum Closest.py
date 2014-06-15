class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        minDiff = 10**10
        ret = 0
        for i in range(len(num)-2):
           left = i+1
           right = len(num)-1
           while left < right:
               s = num[i] + num[left] + num[right]
               diff = abs(s - target)
               if diff < minDiff:
                   minDiff = diff
                   ret = s
               if s == target:
                   return  target
               elif s < target:
                   left +=1
               else :
                   right -= 1
        return ret