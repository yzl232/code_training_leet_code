'''
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
'''
class Solution:
    # @param A, a list of integers    #7123456     2345671
    # @param target, an integer to be searched
    # @return an boolean
    def search(self, arr, target):
        l , h = 0, len(arr)-1
        while l<=h:
            m = (l+h)/2
            if arr[m] == target: return  True
            elif arr[m]>arr[l]:
                if arr[l]<=target<=arr[m]:  h = m-1
                else: l = m+1
            elif arr[m]<arr[l]:
                if arr[m]<=target<=arr[h]:   l = m+1
                else:   h = m-1
            else:    l+=1
        return False