class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, arr):  #就是由i控制窗口的2sum
        arr.sort();    ret = set()
        for i in range(len(arr)-2):  #i一直作为左边界。 逐渐变小的sliding window
            if i>0 and arr[i]==arr[i-1]: continue
            l = i+1; r=len(arr)-1; target = 0-arr[i]
            while l<r:  
                if arr[l]+arr[r] == target:
                    ret.add((arr[i], arr[l], arr[r]))
                    l+=1; r-=1  #同时变化2个pointer
                elif arr[l]+ arr[r]<target: l+=1
                else: r-=1
        return [list(i) for i in ret]
'''
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        d, result = {}, set()
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                if num[i] + num[j] not in d:  d[num[i] + num[j]] = [[num[i], num[j]]]
                else: d[num[i] + num[j]].append([num[i], num[j]])
        for i in range(len(num)-2):
            target = 0-num[i]
            if target in d:
                for k in d[target]:
                    if num[k[0]]>=num[i]:
                        result.add((num[i], k[0], k[1] ))
        return [list(i) for i in result]

'''