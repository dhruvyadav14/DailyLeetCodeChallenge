import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # i mean this is kind of like the same concept as merge meetings right? except i dont want to merge
        # first lets just make an array of tuples, of each meetings start and end time, and profit
        # maybe the idea is, for each meeting, figure out what the profit is. this is n^2 but lets do it

        # combinedArray = []
        # maxP=0
        # n = len(startTime)
        # for i in range(n):
        #     combinedArray.append((startTime[i],endTime[i],profit[i]))

        # print(combinedArray)

        # for s,e,p in combinedArray:


        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        print(jobs)
        dp = [[0, 0]]
        for s, e, p in jobs:
            print("--------------------------------")
            i = bisect.bisect(dp, [s + 1]) - 1
            print(i)
            print("do we enter the if")
            if dp[i][1] + p > dp[-1][1]:
                print("yeah we do")
                print(dp)
                dp.append([e, dp[i][1] + p])
                print(dp)
        return dp[-1][1]
