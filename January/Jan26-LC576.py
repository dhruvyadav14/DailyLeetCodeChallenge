class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def recursive(row, col, moves):
            if moves < 0:
                return 0
            if row < 0 or row >=m or col < 0 or col >= n:
                return 1
            
            return recursive(row-1, col, moves-1) + recursive(row+1, col, moves-1) + recursive(row, col-1, moves-1) + recursive(row, col+1, moves-1)
    
        return recursive(startRow, startColumn, maxMove) % ((10**9) + 7)
    
# why use dp array when i can just use cache decorator lolol