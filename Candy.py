class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):   #自己举出特例就可以看懂解法了
        length = len(ratings)
        candy = [1 for i in range(length)]
        for i in range(length-1):   # right neighbour
            if ratings[i+1] > ratings[i] and candy[i+1] <= candy[i]:
                candy[i+1] = candy[i] + 1
        for i in range(length-1, 0, -1):  # left neighbour
            if ratings[i-1] > ratings[i] and candy[i-1] <= candy[i]:
                candy[i-1] = candy[i]+1
        #print candy  
        return sum(candy)
        
        
        '''
         There are N children standing in a line. Each child is assigned a rating value.

        You are giving candies to these children subjected to the following requirements:

            Each child must have at least one candy.
            Children with a higher rating get more candies than their neighbors.

        What is the minimum candies you must give?
        
        '''