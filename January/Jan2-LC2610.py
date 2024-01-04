from collections import Counter
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        """
        loop through the array 
        if we come across a number that isnt in the subarray, add to subarray
        if we come across a number that IS in subarray, create new subarray
        if we come across a number that isnt in either subarray, add to first?
        if we come across a number that IS in BOTH subarrays, create new subarray
        this will be n2, we are going through each array that will be of length n twice
        BADBADBADBAD!!

        maybe use a map? keep a count of how many times a number appears. everytime we encounter that key, reduce the count?
        loop through map keys? if value of key>0 and key not already in subarray, add to subarray
        basically, while max(map.values)>0, and then inside the while, loop through all keys
        lets try coding
        """

        mymap = Counter(nums)
        k = max(mymap.values())
        ans=[[]]*k
        for i in range(k):
            subarray=[]
            for key in mymap.keys():
                if mymap[key]>0 and key not in subarray:
                    subarray.append(key)
                    mymap[key]-=1
            ans[i]=subarray
        return ans

