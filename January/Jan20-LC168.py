class Solution:
    def rob(self, nums: List[int]) -> int:
        # isnt it just start at the first house or the 2nd house? wtf?
        # sum1 = 0
        # sum2 = 0
        # for i,num in enumerate(nums):
        #     if i%2 == 0:
        #         sum1 += num
        #     else:
        #         sum2 += num
        # return max(sum1,sum2)

        # ahhhh i see. not so simple now. how do i do it
        # this is a variant on max subarray problem. this is a recursion problem
        @cache
        def robHelper(i):
            if i<0:
                return 0
            return max(robHelper(i-2) + nums[i], robHelper(i-1)) 
        return robHelper(len(nums)-1)
