class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        res = []
        for i in range(len(num)-2):
            if i>0 and num[i] == num[i-1]: continue  # duplicates
            left = i+1; right = len(num)-1; target = 0 - num[i]
            while left < right:   #夹逼。不能取等号。 因为left, right不能取同一个数
                if num[left] + num[right] == target:
                    res.append([num[i], num[left], num[right]])
                    left+=1; right -=1
                    while left < right and num[left] == num[left-1]: left+=1  # duplicates
                    while left < right and num[right] == num[right+1]: right-=1  # duplicates
                elif num[left] + num[right] < target:
                    left+=1
                    while left < right and num[left] == num[left-1]: left+=1  # duplicates
                else:
                    right -=1
                    while left < right and num[right] == num[right+1]: right-=1  # duplicates
        return res