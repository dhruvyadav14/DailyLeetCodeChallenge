from collections import Counter 
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # first thought is to create a map counter for each letter
        """
        {c:1, t:1, e:3, l:1, o:1, d:1}
        {c:2, t:1, p:1, r:1, a:1, i:1, e:1}
        """

        
        cnt, steps = Counter(s), 0
        for c in t:
            if cnt[c] > 0:
                cnt[c] -= 1
            else:
                steps += 1
        return steps