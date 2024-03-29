from functools import cache


class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        # fibonacci. also import cache for memoization
        if n==0 or n==1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)