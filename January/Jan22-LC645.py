class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # expected = {num for num in range(1,len(nums)+1)}
        # duplicate = next(item for item in nums if nums.count(item)>1)
        # return [duplicate, (expected-set(nums)).pop()]

        # this code is gross. lets fix it lol

        expectedSum = int((len(nums)*(len(nums)+1))/2)
        actualSum = sum(nums)
        setSum = sum(set(nums))
        missingNum = expectedSum - setSum
        duplicate = abs(expectedSum-actualSum-missingNum)
        return [duplicate,missingNum]
