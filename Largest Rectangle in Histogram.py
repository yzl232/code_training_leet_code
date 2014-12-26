'''
 Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10. 
'''

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, arr):
        stack = []   #stack储存递增的
        arr.append(0)     #加了一个0，  arr[stack[-1]] < arr[i]不会满足。stack一定会全部pop
        i = 0;  ret = 0
        while i<len(arr):
            if not stack or  arr[stack[-1]] < arr[i]:
                stack.append(i)
                i+=1
            else:
                t = stack.pop()
                if stack:  ret = max(arr[t]*(i-1-stack[-1]), ret)
                else:  ret = max(arr[t] * i, ret)     #空stack相当于 -1
        return ret
'''
O(N)解法, 挺明白的。要一个栈来存放非递减的height序列, 即碰到大于等于栈顶的就入栈, 碰到小于栈顶的就pop。对于每个pop出的元素h[stack[top]]，都要计算以它为最低高度的矩形的面积, 高度就是h[stack[top]], 宽度就是i － stack[-1] - 1, 注意栈中的元素都是非递减的。在h末尾多加一个0的目的是保证栈中的元素都可以被pop出
'''