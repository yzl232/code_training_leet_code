class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        result = []
        for i in range(len(num)-2):
            left = i+1; right = len(num)  - 1; target = 0 - num[i]
            while left < right:
                if num[left] + num[right] + num[i] == 0:
                    if [num[i], num[left], num[right]] not in result: result.append([num[i], num[left], num[right]])
                    left+=1; right-=1
                elif num[left] + num[right] < target:
                    left+=1
                else:
                    right-=1
        return result
            