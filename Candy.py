'''
 There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?

'''

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, arr):
        n=len(arr); candy = [1]*n
        for i in range(1, n):
            if arr[i]>arr[i-1]:      candy[i] = max(candy[i-1]+1, candy[i])
        for i in range(n-2, -1, -1):
            if arr[i]>arr[i+1]:     candy[i] = max(candy[i+1]+1, candy[i])
        return sum(candy)
        #从左到右算一遍，ratings递增时candy也递增，否则都只给一块糖。
#再从右到左修正一遍：如果左比右rating高但却没有拿更多的糖，修正。
        
