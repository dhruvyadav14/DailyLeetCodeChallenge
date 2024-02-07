from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countMap=Counter(arr)
        return len({value for value in countMap.values()}) == len([value for value in countMap.values()]) 
        