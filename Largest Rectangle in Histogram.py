'''
 Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10. 
'''

'''
新增理解.  便捷. 发现了很小的右边界R后, 往左找边界.    不断pop, 计算, 知道左边界

栈里边的边界都是递增的.
'''

'''
 Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10. 
'''

'''
新增理解.  便捷. 发现了很小的右边界R后, 往左找边界.    不断pop, 计算, 知道左边界

栈里边的边界都是递增的.
'''


#可以对照下类似写法的create maximum number
class Solution: #核心在于保证stack的递增的左边界。
    # @param height, a list of integer
    # @return an integer     #和next greater element很像  #碰到比arr[i]小的， 不断清除。 自豪再stack.append
    def largestRectangleArea(self, arr):   #  #测试例子用[1, 2]这样最简单的例子
        arr.append(0); ret = 0;  st = []    #stack储存递增的. 也就是必须是递增的左边界
        for r in range(len(arr)):      # 于是到最后i。 不断pop。    保证stack的递增。
            while st and arr[st[-1]]>arr[r]:    ret = max(ret, (arr[st.pop()] )*(r if not st else r - (st[-1]+1)  ))       #
            st.append(r)   # 此时为空或者arr[i]大。 可以append
        return ret   #pop出的就是高度.   #stack的元素只要大于arr[i]. 就不断pop
    #-1理解，  l和r都是面积外面的。 所以要r-l-1
 #左边界加1.  想象方块的左边界。就容易了     
 #空stack相当于 -1,  i=0, 占了长度1， i=1， 占了长度2
#加了一个0，  arr[stack[-1]] < arr[i]不会满足 

# 面积=h*w  .  如果h增加，w增加。 我们不断进行append
#  if h减小，

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

O(N)解法, 挺明白的。要一个栈来存放非递减的height序列, 即碰到大于等于栈顶的就入栈, 碰到小于栈顶的就pop。对于每个pop出的元素h[stack[top]]，都要计算以它为最低高度的矩形的面积, 高度就是h[stack[top]], 宽度就是i － stack[-1] - 1, 注意栈中的元素都是非递减的。在h末尾多加一个0的目的是保证栈中的元素都可以被pop出
'''