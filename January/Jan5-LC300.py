import bisect


class Solution:
    """
    The dumb and inefficient solution is to do nested for loops and find the longest subsequence for each starting index
    This sucks

    Can we use a variation of kadanes algorithm for maxsubarray? in kadanes we figure out what the maximum sum is by keeping track of local and overall maxima
    ACTUALLY - this is sort of like the best time to buy and sell stock problem! what if we just looped through the array, checking to see if current num is > prev num
    if so, increase output. if not....nvm. this algorithm doesnt work. lets just do the dumb solution first
    """

    # def lengthOfLIS(self, nums: List[int]) -> int:
        
    #     dp=[1]*len(nums)
    #     for i in range(len(nums)):
    #         for j in range(i):
    #             if nums[i]>nums[j]:
    #                 dp[i]=max(dp[j]+1,dp[i])

    #     return max(dp)
    i= bisect.bisect([[0, 0], [3, 20]], [-1])
    print(i)