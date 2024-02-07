class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        interesting problem...how do i even approach this? lol
        i suppose i take the min sum of all possible falling paths. this will be brute force
        yeah this is gonna be n^2
        lets loop through matrix. this will be looping through the rows.
        idk...im actually thinking recursion. 
        so now im thinking for loop through matrix, call a new recursive func and pass in [(row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]. 
        in this recursive helper function, the base case if there are no more rows, return min(r+1, col-1, etc...). call the function recursively. then return that min
        to me this looks like DFS!!!
        """

        def helper(row, path):
            if row == len(matrix):
                return 0
            
            updatedPath = []
            for col in path:
                if col < 0 or col >= len(matrix):
                    continue
                updatedPath.append(col)

            pathValues = [matrix[row][col] for col in updatedPath]
            if row == len(matrix)-1:
                return min(pathValues)
            
            for col in updatedPath:
                possiblePath = [col-1,col,col+1]
                x = matrix[row][col] + helper(row+1, possiblePath)
                self.allsums.append(x)
            return min(self.allsums)

        minPathSum = inf
        for i in range(len(matrix)):
            self.allsums = []
            row,col = 0,i
            possiblePath = [i-1,i,i+1]
            minPathSum = min(matrix[0][i] + helper(row + 1, possiblePath), minPathSum)
        return minPathSum
