class Solution:
    def firstUniqChar(self, s: str) -> int:
        # indexMap = {}
        # for i,c in enumerate(s):
        #     if c not in indexMap:
        #         indexMap[c] = i
        #     else:
        #         #tis a dupe.
        #         indexMap[c] = None
        # filtered_map = {key: value for key, value in indexMap.items() if value is not None}
        # if filtered_map: return min(filtered_map.values())
        # return -1


        #heres a better way to do it
        index_map = {}
        for c in s:
            index_map[c] = index_map.get(c,0) + 1

        for i in range(len(s)):
            if index_map[s[i]] == 1:
                return i
        return -1
