class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedMap = defaultdict(list)
        for word in strs:
            sortedWord = ''.join(sorted(word))
            sortedMap[sortedWord].append(word)

        return [values for values in sortedMap.values()]
