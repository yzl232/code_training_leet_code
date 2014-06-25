class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        left = 0; right = m * n - 1
        while left <= right:
            mid = (left + right) / 2
            value = matrix[mid/n][mid%n]
            if value == target: return True
            elif value > target: right = mid-1
            else: left = mid + 1
        return False