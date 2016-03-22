'''
 Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
'''
'''
[2, 1, 0]
return [0, 1, 2]

[1]  return [1]
'''


class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, arr):
        p2 = len(arr) - 1
        p0 = 0
        i = 0
        while i<= p2:   #取等号. 因为就算到达了, p2只是保证了p2后面的. a[p2]仍然可能为0
            while p2 >= i and arr[i] == 2:
                arr[i], arr[p2] = arr[p2], arr[i]
                p2 -=1
            while p0<=i and arr[i] == 0:
                arr[i], arr[p0] = arr[p0], arr[i]
                p0+=1
            i+=1
# 第一个while 保证了 p2后面全是2，  i前面没有2
# 第二个while保证了 p0前面全是0.   p0~i之间没有0



'''
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, arr):
        i =p1=0; p2 = len(arr) -1  # p1 points to first 1, p2 points to the one before first 2.
        while i <= p2:     # #0 is before p1,  2 is after p2.
            if arr[i] == 2:
                arr[p2], arr[i] = arr[i], arr[p2] #i-=1   不知道过来啥颜色
                p2 -= 1; i-=1
            elif arr[i] == 0:  # A[i] always get 1, since 0 is before p0,  2 is after p2.
                arr[p1], arr[i] = arr[i], arr[p1]  #因为前面不可能有2. 缓过来1
                p1+=1  #p1总在I左边
            i+=1

#关于p1. 可以看出 p1总在I左边。  它与i相差1的数目。 也就是指向第一个1。
'''